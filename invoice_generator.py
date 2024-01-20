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

    pdf.set_font(family="Times", style="B", size=14)
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

    # add header
    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.cell(w=25, h=10, txt=columns[0], border=1)
    pdf.cell(w=55, h=10, txt=columns[1], border=1)
    pdf.cell(w=50, h=10, txt=columns[2], border=1)
    pdf.cell(w=40, h=10, txt=columns[3], border=1)
    pdf.cell(w=25, h=10, txt=columns[4], border=1, ln=1)
    # add  columns
    for index, row in df.iterrows():
        pdf.set_font(family="Times", size=14)
        pdf.cell(w=25, h=10, txt=str(row['product_id']), border=1)
        pdf.cell(w=55, h=10, txt=str(row['product_name']), border=1)
        pdf.cell(w=50, h=10, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=40, h=10, txt=str(row['price_per_unit']), border=1)
        pdf.cell(w=25, h=10, txt=str(row['total_price']), border=1, ln=1)

    # add total price
    pdf.set_font(family="Times", size=14)
    pdf.cell(w=25, h=10, txt="", border=1)
    pdf.cell(w=55, h=10, txt="", border=1)
    pdf.cell(w=50, h=10, txt="", border=1)
    pdf.cell(w=40, h=10, txt="", border=1)
    pdf.cell(w=25, h=10, txt=str(df["total_price"].sum()), border=1, ln=1)

    # add text
    pdf.cell(w=0, h=14, txt=f"The total due amount is {df['total_price'].sum()} Euros", ln=1)

    # add company name and logo
    pdf.cell(w=27, h=14, txt="Abhinesh.org".title())
    pdf.image("logo1.png", w=20, h=20)

    pdf.output(f"pdf/{filename}.pdf")







