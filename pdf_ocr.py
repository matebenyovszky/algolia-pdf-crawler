# Add error handling and logging
import requests
import logging

def run_ocr_on_pdf(pdf_url):
    try:
        # Replace <your_api_key> with your actual API key
        api_key = os.environ.get('FORM_RECOGNIZER_API_KEY')
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
    except Exception as e:
        logging.error(f'Error occurred while running OCR on PDF: {e}')



#### Ez már talán nem fog kelleni

import os
import requests
from io import BytesIO
from dotenv import load_dotenv
#from azure.ai.formrecognizer import DocumentAnalysisClient
#from azure.core.credentials import AzureKeyCredential

def scrape_pdf(data):
    # Load environment variables from .env file
    load_dotenv()

    # Get OCR API credentials from environment variables
    ocr_api_key = os.getenv("OCR_API_KEY")
    ocr_endpoint = os.getenv("OCR_ENDPOINT")

    # Create an instance of the DocumentAnalysisClient
    credential = AzureKeyCredential(ocr_api_key)
    client = DocumentAnalysisClient(endpoint=ocr_endpoint, credential=credential)

    for file_url in data.get("file_urls", []):
        # Download the file from the URL
        response = requests.get(file_url)
        if response.status_code == 200:
            # Open the downloaded file as an image


            # Extract the recognized text from the OCR result
            recognized_text = ""
            for page in result.pages:
                for line in page.lines:
                    recognized_text += line.text + " "

            # Add the recognized text to the data dictionary
            data["recognized_text"] = recognized_text

    return data
