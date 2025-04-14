import pandas as pd
import json
from pandas import json_normalize

def get_dataframe(json_file_path='dataset.json'):
    """
    Creates a DataFrame from a complex JSON file with nested structures like dictionaries and lists.
    
    Args:
        json_file_path (str): Path to the JSON file
        
    Returns:
        pandas.DataFrame: A properly formatted DataFrame containing all the data
    """
    # Read the JSON file
    with open(json_file_path, 'r') as file:
        data = json.load(file)
    
    # Handle different JSON structures
    if isinstance(data, dict):
        # Case 1: JSON with a list under a specific key (like 'employees')
        for key, value in data.items():
            if isinstance(value, list) and all(isinstance(item, dict) for item in value):
                # Create DataFrame from the list of dictionaries
                df = pd.DataFrame(value)
                
                # Add information from other keys as columns
                for other_key, other_value in data.items():
                    if other_key != key:
                        if isinstance(other_value, dict):
                            # Flatten nested dictionaries and add as columns
                            for sub_key, sub_value in other_value.items():
                                df[f"{other_key}_{sub_key}"] = sub_value
                        else:
                            # Add simple values as columns
                            df[other_key] = other_value
                
                return df
        
        # Case 2: No suitable list found, normalize the entire dictionary
        return json_normalize(data)
    
    # Case 3: JSON is a list of dictionaries
    elif isinstance(data, list) and all(isinstance(item, dict) for item in data):
        return pd.DataFrame(data)
    
    # Case 4: JSON is a list with mixed content
    elif isinstance(data, list):
        return pd.DataFrame({'data': data})
    
    else:
        raise ValueError("Unsupported JSON structure")
