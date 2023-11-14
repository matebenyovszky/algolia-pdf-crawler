import requests
from bs4 import BeautifulSoup
import re

def get_linked_pdfs(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    pdf_links = []
    
    # Find all anchor tags (links) in the page
    for a_tag in soup.find_all('a', href=True):
        href = a_tag['href']
        
        # Check if the link ends with '.pdf'
        if href.endswith('.pdf'):
            # If it's a PDF link, append it to the pdf_links list
            pdf_links.append(href)
    
    return pdf_links
