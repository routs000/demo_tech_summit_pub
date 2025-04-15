# import numpy as np

# import matplotlib.pyplot as plt


# def create_line_plot(x, y, title='Line Plot', xlabel='X Axis', ylabel='Y Axis', 
#                      color='blue', marker='o', linestyle='-', figsize=(10, 6), 
#                      grid=True, save_path=None):
#     """
#     Create a line plot with customizable parameters.
    
#     Parameters:
#     -----------
#     x : array-like
#         The x coordinates of the plotted data
#     y : array-like
#         The y coordinates of the plotted data
#     title : str
#         Title of the plot
#     xlabel : str
#         Label for the x-axis
#     ylabel : str
#         Label for the y-axis
#     color : str
#         Color of the line
#     marker : str
#         Marker style
#     linestyle : str
#         Line style
#     figsize : tuple
#         Figure size (width, height) in inches
#     grid : bool
#         Whether to show grid lines
#     save_path : str, optional
#         If provided, save the figure to this path
    
#     Returns:
#     --------
#     fig, ax : tuple
#         The figure and axis objects
#     """
#     chart_name = "Line Chart"
#     chart_file = "line_chart.png"
#     image_url = f"https://github.com/routs000/demo_tech_summit/blob/gh-pages/output_images/{chart_file}?raw=true"
#     fig, ax = plt.subplots(figsize=figsize)
#     ax.plot(x, y, color=color, marker=marker, linestyle=linestyle)
#     ax.set_title(title)
#     ax.set_xlabel(xlabel)
#     ax.set_ylabel(ylabel)
#     ax.grid(grid)
    
#     if save_path:
#         plt.savefig(f'{save_path}/{chart_file}', bbox_inches='tight')
    
#     return {
#         "chart_name": chart_name,
#         "image_url": image_url
#     }

# def create_scatter_plot(x, y, title='Scatter Plot', xlabel='X Axis', ylabel='Y Axis', 
#                        color='blue', marker='o', alpha=0.7, figsize=(10, 6), 
#                        grid=True, save_path=None):
#     """
#     Create a scatter plot with customizable parameters.
    
#     Parameters:
#     -----------
#     x : array-like
#         The x coordinates of the plotted data
#     y : array-like
#         The y coordinates of the plotted data
#     title : str
#         Title of the plot
#     xlabel : str
#         Label for the x-axis
#     ylabel : str
#         Label for the y-axis
#     color : str or array-like
#         Color(s) of the scatter points
#     marker : str
#         Marker style
#     alpha : float
#         Transparency level (0 to 1)
#     figsize : tuple
#         Figure size (width, height) in inches
#     grid : bool
#         Whether to show grid lines
#     save_path : str, optional
#         If provided, save the figure to this path
    
#     Returns:
#     --------
#     fig, ax : tuple
#         The figure and axis objects
#     """
#     chart_name = "Scatter Chart"
#     chart_file = f"scatter_chart.png"
#     image_url = f"https://github.com/routs000/demo_tech_summit/blob/gh-pages/output_images/{chart_file}?raw=true"
#     fig, ax = plt.subplots(figsize=figsize)
#     ax.scatter(x, y, color=color, marker=marker, alpha=alpha)
#     ax.set_title(title)
#     ax.set_xlabel(xlabel)
#     ax.set_ylabel(ylabel)
#     ax.grid(grid)
    
#     if save_path:
#         plt.savefig(f'{save_path}/{chart_file}', bbox_inches='tight')
    
#     return {
#         "chart_name": chart_name,
#         "image_url": image_url
#     }

# def create_pie_plot(sizes, labels=None, title='Pie Chart', colors=None, 
#                    autopct='%1.1f%%', startangle=90, figsize=(10, 10), 
#                    shadow=False, explode=None, save_path=None):
#     """
#     Create a pie chart with customizable parameters.
    
#     Parameters:
#     -----------
#     sizes : array-like
#         The wedge sizes
#     labels : array-like, optional
#         The wedge labels
#     title : str
#         Title of the plot
#     colors : array-like, optional
#         The colors for each wedge
#     autopct : str, optional
#         Format string for wedge values
#     startangle : int
#         Starting angle for wedges
#     figsize : tuple
#         Figure size (width, height) in inches
#     shadow : bool
#         Whether to draw a shadow beneath the pie
#     explode : array-like, optional
#         Fraction of radius to offset each wedge
#     save_path : str, optional
#         If provided, save the figure to this path
    
#     Returns:
#     --------
#     fig, ax : tuple
#         The figure and axis objects
#     """
#     chart_name = "Pie Chart"
#     chart_file = f"pie_chart.png"
#     image_url = f"https://github.com/routs000/demo_tech_summit/blob/gh-pages/output_images/{chart_file}?raw=true"
#     fig, ax = plt.subplots(figsize=figsize)
#     ax.pie(sizes, labels=labels, colors=colors, autopct=autopct, 
#            startangle=startangle, shadow=shadow, explode=explode)
#     ax.set_title(title)
#     ax.axis('equal')  # Equal aspect ratio ensures pie is circular
    
#     if save_path:
#         plt.savefig(f'{save_path}/{chart_file}', bbox_inches='tight')
    
#     return {
#         "chart_name": chart_name,
#         "image_url": image_url
#     }


import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import os


def create_line_plot(x, y, title='Line Plot', xlabel='X Axis', ylabel='Y Axis',
                     color='blue', marker='circle', linestyle='solid',
                     grid=True, save_path=None):
    """
    Create a line plot with customizable parameters using Plotly.
    
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
        Marker style (circle, square, diamond, etc.)
    linestyle : str
        Line style (solid, dash, dot, etc.)
    figsize : tuple
        Figure size (width, height) in pixels
    grid : bool
        Whether to show grid lines
    save_path : str, optional
        If provided, save the figure to this path
    
    Returns:
    --------
    dict
        Chart metadata
    """
    chart_name = "Line Chart"
    chart_file = "line_chart.html"
    image_url = f"https://routs000.github.io/demo_tech_summit_pub/output_images/{chart_file}"
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='lines+markers',
        marker=dict(symbol=marker, color=color),
        line=dict(dash=linestyle, color=color)
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        autosize=True,
        template='plotly_white' if grid else 'plotly'
    )
    
    if save_path:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        fig.write_html(f'{save_path}/{chart_file}')
    
    return {
        "chart_name": chart_name,
        "image_url": image_url
    }


def create_scatter_plot(x, y, title='Scatter Plot', xlabel='X Axis', ylabel='Y Axis',
                       color='blue', marker='circle', alpha=0.7,
                       grid=True, save_path=None):
    """
    Create a scatter plot with customizable parameters using Plotly.
    
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
        Color of the scatter points
    marker : str
        Marker symbol
    alpha : float
        Opacity level (0 to 1)
    figsize : tuple
        Figure size (width, height) in pixels
    grid : bool
        Whether to show grid lines
    save_path : str, optional
        If provided, save the figure to this path
    
    Returns:
    --------
    dict
        Chart metadata
    """
    chart_name = "Scatter Chart"
    chart_file = "scatter_chart.html"
    image_url = f"https://routs000.github.io/demo_tech_summit_pub/output_images/{chart_file}"
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode='markers',
        marker=dict(
            symbol=marker,
            color=color,
            opacity=alpha
        )
    ))
    
    fig.update_layout(
        title=title,
        xaxis_title=xlabel,
        yaxis_title=ylabel,
        autozise=True,
        template='plotly_white' if grid else 'plotly'
    )
    
    if save_path:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        fig.write_html(f'{save_path}/{chart_file}')
    
    return {
        "chart_name": chart_name,
        "image_url": image_url
    }


def create_pie_plot(sizes, labels=None, title='Pie Chart', colors=None,
                   textinfo='percent+label', startangle=90,
                   hole=0, pull=None, save_path=None):
    """
    Create a pie chart with customizable parameters using Plotly.
    
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
    textinfo : str, optional
        Format for text ('percent', 'label', 'value', or combinations with '+')
    startangle : int
        Starting angle for wedges in degrees (not directly supported in Plotly)
    figsize : tuple
        Figure size (width, height) in pixels
    hole : float
        Size of hole in the middle (0-1) for donut charts
    pull : array-like, optional
        Fraction to pull each wedge out from center
    save_path : str, optional
        If provided, save the figure to this path
    
    Returns:
    --------
    dict
        Chart metadata
    """
    chart_name = "Pie Chart"
    chart_file = "pie_chart.html"
    image_url = f"https://routs000.github.io/demo_tech_summit_pub/output_images/{chart_file}"
    
    fig = go.Figure(data=[go.Pie(
        labels=labels,
        values=sizes,
        textinfo=textinfo,
        hoverinfo='label+percent+value',
        hole=hole,
        pull=pull,
        marker_colors=colors
    )])
    
    fig.update_layout(
        title=title,
        autosize=True,
    )
    
    if save_path:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        fig.write_html(f'{save_path}/{chart_file}')
    
    return {
        "chart_name": chart_name,
        "image_url": image_url
    }
