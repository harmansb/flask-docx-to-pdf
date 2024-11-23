from flask import render_template, request, send_file
from app import app
from app.utils.metadata_extractor import extract_metadata
from app.utils.pdf_converter import convert_to_pdf
from app.utils.pdf_protector import protect_pdf
import os

UPLOAD_FOLDER = os.path.join(app.root_path, "uploads")  # Correctly resolve the upload folder
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["file"]
        if uploaded_file.filename.endswith(".docx"):
            filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.filename)
            uploaded_file.save(filepath)

            metadata = extract_metadata(filepath)
            pdf_filepath = convert_to_pdf(filepath)
            secure_pdf_filepath = protect_pdf(pdf_filepath, "securepassword")

            return render_template(
                "result.html",
                metadata=metadata,
                pdf_file=os.path.relpath(secure_pdf_filepath, start=app.root_path),  # Return relative path
            )
        return "Error: Only .docx files are allowed", 400
    return render_template("index.html")


@app.route("/download/<path:filename>")
def download(filename):
    # Resolve the full path of the file
    full_path = os.path.join(app.root_path, filename)
    return send_file(full_path, as_attachment=True)
