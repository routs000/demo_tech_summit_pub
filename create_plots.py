import numpy as np

import matplotlib.pyplot as plt


def create_line_plot(x, y, title='Line Plot', xlabel='X Axis', ylabel='Y Axis', 
                     color='blue', marker='o', linestyle='-', figsize=(10, 6), 
                     grid=True, save_path=None):
    """
    Create a line plot with customizable parameters.
    
    Parameters:
    -----------
    x : array-like
        The x coordinates of the plotted data
    y : array-like
        The y coordinates of the plotted data
    title : str
        Title of the plot
    xlabel : str
        Label for the x-axis
    ylabel : str
        Label for the y-axis
    color : str
        Color of the line
    marker : str
        Marker style
    linestyle : str
        Line style
    figsize : tuple
        Figure size (width, height) in inches
    grid : bool
        Whether to show grid lines
    save_path : str, optional
        If provided, save the figure to this path
    
    Returns:
    --------
    fig, ax : tuple
        The figure and axis objects
    """
    chart_name = "Line Chart"
    chart_file = "line_chart.png"
    image_url = f"https://github.com/routs000/demo_tech_summit/blob/gh-pages/output_images/{chart_file}?raw=true"
    fig, ax = plt.subplots(figsize=figsize)
    ax.plot(x, y, color=color, marker=marker, linestyle=linestyle)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)
    
    if save_path:
        plt.savefig(f'{save_path}/{chart_file}', bbox_inches='tight')
    
    return {
        "chart_name": chart_name,
        "image_url": image_url
    }

def create_scatter_plot(x, y, title='Scatter Plot', xlabel='X Axis', ylabel='Y Axis', 
                       color='blue', marker='o', alpha=0.7, figsize=(10, 6), 
                       grid=True, save_path=None):
    """
    Create a scatter plot with customizable parameters.
    
    Parameters:
    -----------
    x : array-like
        The x coordinates of the plotted data
    y : array-like
        The y coordinates of the plotted data
    title : str
        Title of the plot
    xlabel : str
        Label for the x-axis
    ylabel : str
        Label for the y-axis
    color : str or array-like
        Color(s) of the scatter points
    marker : str
        Marker style
    alpha : float
        Transparency level (0 to 1)
    figsize : tuple
        Figure size (width, height) in inches
    grid : bool
        Whether to show grid lines
    save_path : str, optional
        If provided, save the figure to this path
    
    Returns:
    --------
    fig, ax : tuple
        The figure and axis objects
    """
    chart_name = "Scatter Chart"
    chart_file = f"scatter_chart.png"
    image_url = f"https://github.com/routs000/demo_tech_summit/blob/gh-pages/output_images/{chart_file}?raw=true"
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(x, y, color=color, marker=marker, alpha=alpha)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.grid(grid)
    
    if save_path:
        plt.savefig(f'{save_path}/{chart_file}', bbox_inches='tight')
    
    return {
        "chart_name": chart_name,
        "image_url": image_url
    }

def create_pie_plot(sizes, labels=None, title='Pie Chart', colors=None, 
                   autopct='%1.1f%%', startangle=90, figsize=(10, 10), 
                   shadow=False, explode=None, save_path=None):
    """
    Create a pie chart with customizable parameters.
    
    Parameters:
    -----------
    sizes : array-like
        The wedge sizes
    labels : array-like, optional
        The wedge labels
    title : str
        Title of the plot
    colors : array-like, optional
        The colors for each wedge
    autopct : str, optional
        Format string for wedge values
    startangle : int
        Starting angle for wedges
    figsize : tuple
        Figure size (width, height) in inches
    shadow : bool
        Whether to draw a shadow beneath the pie
    explode : array-like, optional
        Fraction of radius to offset each wedge
    save_path : str, optional
        If provided, save the figure to this path
    
    Returns:
    --------
    fig, ax : tuple
        The figure and axis objects
    """
    chart_name = "Pie Chart"
    chart_file = f"pie_chart.png"
    image_url = f"https://github.com/routs000/demo_tech_summit/blob/gh-pages/output_images/{chart_file}?raw=true"
    fig, ax = plt.subplots(figsize=figsize)
    ax.pie(sizes, labels=labels, colors=colors, autopct=autopct, 
           startangle=startangle, shadow=shadow, explode=explode)
    ax.set_title(title)
    ax.axis('equal')  # Equal aspect ratio ensures pie is circular
    
    if save_path:
        plt.savefig(f'{save_path}/{chart_file}', bbox_inches='tight')
    
    return {
        "chart_name": chart_name,
        "image_url": image_url
    }