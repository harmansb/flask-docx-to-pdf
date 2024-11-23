import os
from PyPDF2 import PdfWriter
from app import app

def protect_pdf(pdf_path, password):
    writer = PdfWriter()
    writer.append(pdf_path)
    writer.encrypt(password)

   
    protected_path = os.path.join(app.root_path, "uploads", os.path.basename(pdf_path).replace(".pdf", "_protected.pdf"))
    
    with open(protected_path, "wb") as f:
        writer.write(f)
        
    return protected_path
