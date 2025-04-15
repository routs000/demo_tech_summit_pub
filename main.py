import os
import json
from get_data import get_dataframe
from create_plots import create_line_plot, create_scatter_plot, create_pie_plot
import matplotlib.pyplot as plt
import pandas as pd


df = get_dataframe()
print(df)
save_path = 'output_images'
metadata = []
metadata.append(create_line_plot(x=df['name'], y=df['age'], title='Line Plot', xlabel='X Axis', ylabel='Y Axis', save_path=save_path))
metadata.append(create_scatter_plot(x=df['department'], y=df['age'], title='Scatter Plot', xlabel='X Axis', ylabel='Y Axis', save_path=save_path))
metadata.append(create_pie_plot(df['age'], title='Pie Chart', save_path=save_path))
# ... add more chart calls as needed

# Convert the metadata list to JSON and write to file
with open("chart_metadata.json", "w") as f:
    json.dump(metadata, f, indent=2, ensure_ascii=False)
print("Metadata saved to chart_metadata.json")
