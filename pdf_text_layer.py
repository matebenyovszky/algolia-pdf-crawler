# TO BE INTEGRATED !!!!!!!!!!!!!!!!!!!!!!!!!!!!!

import fitz

def get_text_layer_pages(pdf_path):
    doc = fitz.open(pdf_path)
    text_layer_pages = []
    for page_number in range(len(doc)):
        page = doc.load_page(page_number)
        if "text" in page.get_text("dict"):
            text_layer_pages.append(page_number + 1)  # Add 1 to convert from 0-based index to 1-based index
    return text_layer_pages

# Example usage
pdf_path = "path_to_your_pdf.pdf"
pages_with_text_layer = get_text_layer_pages(pdf_path)
print("Pages with text layer:", pages_with_text_layer)