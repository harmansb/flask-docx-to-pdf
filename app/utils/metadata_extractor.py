from docx import Document

def extract_metadata(docx_path):
    doc = Document(docx_path)
    core_properties = doc.core_properties

    return {
        "author": core_properties.author,
        "title": core_properties.title,
        "created": core_properties.created,
        "modified": core_properties.modified,
    }
