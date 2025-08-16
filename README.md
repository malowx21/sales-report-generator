# Sales-report-generator

# 1- Description
This project generates a sales report in PDF format with charts based on CSV data using Python, Pandas , Matplotlib and FPDF.

# 2- Project Structure 

generateurpdf/
│
├─ example/      # Contains data files (CSV)
│   ├─ first.csv 
│   ├─ second.csv
│   └─ third.csv             
├─ src/               
│   ├─ chart.py  # Create the bar chart 
│   ├─ pdf_class.py  # Creates the PDF
|   └─ report.py     # Adds the sales tables and the date  
├─ main.py       
├─ README.md          
└─ requirements.txt    # Required Python libraries

# 3- What I learned

During this project I learned data manipulation with Pandas and also creating charts whith Matplotlib. I discovered how to generate custom PDFs with FPDF( header, footer, fonts, image insertion)

# 4- Possible improvements

- Add interactive charts
- Support multiple types of reports
- Create a simple user interface
