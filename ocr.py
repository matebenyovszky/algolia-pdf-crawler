import requests
import os

def run_ocr_on_pdf(pdf_url):
    # Replace <your_api_key> with your actual API key
    api_key = '<your_api_key>'
    endpoint = 'https://api.cognitive.microsoft.com/formrecognizer/v2.1-preview.3/prebuilt/receipt/analyze'    
    
    headers = {
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': api_key,
    }
    
    # Prepare the request body with the PDF URL
    body = {
        'source': pdf_url
    }
    
    # Send the request to the Document Intelligence service for OCR
    response = requests.post(endpoint, headers=headers, json=body)
    
    # Get OCR results
    ocr_results = response.json()
    
    return ocr_results
