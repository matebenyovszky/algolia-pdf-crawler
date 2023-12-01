
# import libraries
import os
import datetime
from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential

"""
Cool sites:
https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/concept-read?view=doc-intel-3.1.0
https://westus.dev.cognitive.microsoft.com/docs/services/form-recognizer-api-2023-07-31/operations/AnalyzeDocument
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-v3-python-sdk
"""

# use your `key` and `endpoint` environment variables
key = os.getenv('microsoft_di_key')
endpoint = os.getenv('microsoft_di_endpoint')

def run_ocr_on_pdf(pdf_links, language, base_url):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
    result_dict = []
    for link in pdf_links:
        url = link[0]  # Extracting the URL from the tuple
        print(f"Pages processed (OCR): {len(result_dict)}", end='\r')
        full_url = base_url + url
        poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-read", full_url)
        result = poller.result()

        # Create a dictionary to store the results
        #result_dict = {}
        #result_dict["engine"] = 'microsoft_di'
        #result_dict["content"] = result.content
        #result_dict["pages"] = []
        #result_dict["paragraphs"] = []
        
        for page in result.pages:
            page_dict = {}
            page_dict["type"] = 'pdf'
            page_dict["language"] = language
            page_dict["path"] = url
            #page_dict["title"] = f"(PDF) {os.path.basename(url).split('.')[0]}.pdf" # First line of the PDF
            page_dict["title"] = f"{link[1]} (PDF)"
            page_dict["excerpt"] = '' # Needed so SimplyStatic won't show undefined
            #if page.lines:
            #    page_dict["excerpt"] = page.lines[0].content
            page_dict["objectID"] = f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}{page.page_number}"

            content = ""
            for line in page.lines:
                content += line.content + " "
            page_dict["content"] = content.strip()

            #result_dict["pages"].append(page_dict)
            result_dict.append(page_dict)

        #result_dicts.append(result_dict)

    return result_dict
