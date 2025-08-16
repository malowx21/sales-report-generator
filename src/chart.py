#!/usr/bin/env python3

"""
Import of the modules os and matplotlib.pyplot
"""
import os
import matplotlib.pyplot as plt

def chart_creation(data, csv_file=None):
    """
    Create a bar chart from DataFrame data
    """
    # Define output file name
    if csv_file:
        base_name = os.path.splitext(os.path.basename(csv_file))[0]
        chart_file = f"{base_name}.png"
    else:
        chart_file = "chart.png"
    
    # Create bar chart
    plt.bar(data['Name'], data['Sales'], color='green')
    plt.xlabel('Name')
    plt.ylabel('Sales')
    plt.title('Sales per person')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_file)
    plt.close()
    return chart_file

