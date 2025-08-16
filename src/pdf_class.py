#!/usr/bin/env python3

"""
Importing the module FPDF from the library fpdf
"""
from fpdf import FPDF

class PDF(FPDF):
    """
    Add a header and a footer to the PDF
    """
    def header(self):
        """
        Add a header with title text.
        """
        self.set_font('Times', 'B', 16)
        self.set_text_color(50, 50, 150)
        self.cell(0, 10, 'Sales Report', ln=True, align='C')
        self.ln(10)
    def footer(self):
        """
        Add a footer with page number.
        """
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')
