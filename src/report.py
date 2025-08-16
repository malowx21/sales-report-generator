#!/usr/bin/env python3

"""
Import of the module datetime
"""
import datetime

def sales_table(pdf, data):
    """
    Add sales table to the PDF
    """
    pdf.set_font("Times",'B', 12)
    pdf.cell(60,10,"Name", 1)
    pdf.cell(40,10,"Sales", 1)
    pdf.ln()
    pdf.set_font("Arial", '', 12)
    for _ , row in data.iterrows():
        pdf.cell(60,10, row['Name'],1)
        pdf.cell(40,10, str(row['Sales']),1)
        pdf.ln()
    pdf.ln(10)

def date_report(pdf):
    """
    Add the current date to the PDF
    """
    today= datetime.date.today().strftime("%d/%m/%Y")
    pdf.set_font('Times','', 12)
    pdf.cell(0, 10, f'Report date: {today}', ln=True)
    pdf.ln(10)
