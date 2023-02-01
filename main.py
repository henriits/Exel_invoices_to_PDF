import pandas as pd
import glob
# openepyxl package required
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*xlsx")
# print(filepaths)


for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=False, margin=0)
    pdf.add_page()

    # This allows to get the filename
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Invoice nr. {invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16,style="B")
    pdf.cell(w=50,h=8,txt=f"Date . {date}")




    pdf.output(f"PDFs/{filename}.pdf")