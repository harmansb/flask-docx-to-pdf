from fpdf import FPDF
from docx import Document
import os

def convert_to_pdf(docx_path):
    pdf_path = docx_path.replace(".docx", ".pdf")
    doc = Document(docx_path)

    pdf = FPDF()
    pdf.add_page()

   
    font_path = os.path.join("app", "static", "DejaVuSans.ttf")
    pdf.add_font("DejaVu", style="", fname=font_path, uni=True)
    pdf.set_font("DejaVu", size=12)

   
    for para in doc.paragraphs:
        pdf.multi_cell(0, 10, txt=para.text)  

    pdf.output(pdf_path)
    return pdf_path
