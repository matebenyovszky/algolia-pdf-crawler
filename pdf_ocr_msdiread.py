
# import libraries
import os
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

def run_ocr_on_pdf(file_url):
    document_analysis_client = DocumentAnalysisClient(
        endpoint=endpoint, credential=AzureKeyCredential(key)
    )
    
    poller = document_analysis_client.begin_analyze_document_from_url(
            "prebuilt-read", file_url)
    result = poller.result()

    # Create a dictionary to store the results
    result_dict = {}
    result_dict["engine"] = 'microsoft_di'
    result_dict["content"] = result.content
    result_dict["pages"] = []
    result_dict["paragraphs"] = []
    
    for page in result.pages:
        page_dict = {}
        page_dict["pnum"] = page.page_number

        content = ""
        for line in page.lines:
            content += line.content + " "
        page_dict["pcontent"] = content.strip()

        result_dict["pages"].append(page_dict)

    for idx, paragraph in enumerate(result.paragraphs):
        paragraph_dict = {}
        paragraph_dict["prgnum"] = idx+1
        paragraph_dict["prgcontent"] = paragraph.content

        result_dict["paragraphs"].append(paragraph_dict)

    return result_dict