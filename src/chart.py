import matplotlib.pyplot as plt
import os

def chart_creation(data, csv_file=None):
    """
    Create a bar chart from DataFrame `data`.
    If csv_file is provided, chart name is based on it; otherwise defaults to chart.png.
    Returns the chart filename.
    """
    # Générer le nom du chart automatiquement selon le CSV
    if csv_file:
        base_name = os.path.splitext(os.path.basename(csv_file))[0]
        chart_file = f"{base_name}.png"
    else:
        chart_file = "chart.png"
    
    # Créer le graphique
    plt.bar(data['Name'], data['Sales'], color='green')
    plt.xlabel('Name')
    plt.ylabel('Sales')
    plt.title('Sales per person')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(chart_file)
    plt.close()
    
    return chart_file

