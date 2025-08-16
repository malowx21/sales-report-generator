#!/usr/bin/env python3

import sys
import pandas as pd
from src.pdf_class import PDF
from src.chart import chart_creation
from src.report import date_report, sales_table

def main():
    if len(sys.argv)  < 2:
        print("Respect the syntaxe : python main.py csv_file")
        sys.exit(1)

    csv_file= sys.argv[1]

    try:
        data= pd.read_csv(csv_file)
    except FileNotFoundError:
        print("Error")
        sys.exit(1)

    chart_file= chart_creation(data, csv_file)

    pdf=PDF()
    pdf.add_page()

    date_report(pdf)
    sales_table(pdf,data)

    pdf.image(chart_file, x=30, w=150)

    output_pdf = csv_file.replace(".csv", "_report.pdf")
    pdf.output(output_pdf)

    print(f"The PDF report '{output_pdf}' has been successfully generated!")

if __name__ == "__main__":
    main()
