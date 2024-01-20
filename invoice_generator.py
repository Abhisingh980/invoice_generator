from fpdf import FPDF
import pandas as pd
import pathlib as plib
import glob
import datetime as dt

filepaths = glob.glob("excersis/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    # pdf.set_auto_page_break(auto=False, margin=10)

    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 180, 160)
    filename = plib.Path(filepath).stem
    invoice_no, date = filename.split("-")
    pdf.cell(w=0, h=10, txt=f"Invoice number. {invoice_no}", align="L", ln=1)
    # date tme object
    # x = dt.datetime.now()
    # year = x.year
    # month = x.month
    # day = x.day
    pdf.cell(w=0, h=10, txt=f"Date : {date}", align="L", ln=1)
    # for index, row in df.iterrows():
    #     pdf.cell(w=0, h=10, txt=f"{row['product_id']} | ", align="L", ln=1, border=1)
    pdf.output(f"pdf/{filename}.pdf")







