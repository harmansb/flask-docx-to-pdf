from docx import Document

def extract_metadata(file_path):
    doc = Document(file_path)
    core_properties = doc.core_properties
    return {
        "Title": core_properties.title,
        "Author": core_properties.author,
        "Last Modified By": core_properties.last_modified_by,
        "Created": core_properties.created,
    }
