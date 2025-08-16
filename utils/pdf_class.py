
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Times', 'B', 16)
        self.set_text_color(50, 50, 150)
        self.cell(0, 10, 'Sales Report', ln=True, align='C')
        self.ln(10)
    def footer(self):
        self.set_y(-15)
        self.set_font('Times', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')