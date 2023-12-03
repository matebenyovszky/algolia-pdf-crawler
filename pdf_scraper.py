import os
import requests
from bs4 import BeautifulSoup

def is_file_url(url):
    # Split the URL into parts based on the slash
    parts = url.split('/')
    
    # Get the last part of the URL
    last_part = parts[-1] if parts else ''
    
    # Check if the last part contains a period
    return '.' in last_part

def get_pdf_links(url, base_url, skip_url):
    # Send a GET request to the URL
    response = requests.get(url).content
    
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response, 'html.parser')
    
    pdf_links = []
    num_a_tags = 0
    num_pdf_links = 0

    for a_tag in soup.find_all('a', href=True):
        num_a_tags += 1
        print(f"  Number of links found: {num_a_tags}", end='\r')
        href = a_tag['href']
        if href.startswith("/"):
            href = base_url + href
            # Skip href where href starts with skip_url
            if href.startswith(skip_url):
                continue
                
            # Check if the link ends with '.pdf'
            if href.endswith('.pdf'):
                # If it's a PDF link, append it to the pdf_links list, also add the link title
                if not a_tag.text or a_tag.text.strip() == '' or a_tag.text.startswith("<"):
                    file_name = os.path.basename(href).replace('_', ' ').replace('-', ' ')
                    pdf_links.append((href, file_name))
                else:
                    pdf_links.append((href, a_tag.text))  # Save the href and the text from the a tag

                num_pdf_links += 1
        
            # Check if the link is an internal hyperlink (same domain name)
            elif (href.startswith(url)) and not is_file_url(href):
                # If it's an internal hyperlink and not "/", scrape the linked HTML page
                linked_html = requests.get(href).content
                linked_soup = BeautifulSoup(linked_html, 'html.parser')
                    
                # Find all anchor tags (links) in the linked HTML page
                for linked_a_tag in linked_soup.find_all('a', href=True):
                    linked_href = linked_a_tag['href']
                        
                    # Check if the link ends with '.pdf'
                    if linked_href.endswith('.pdf') and not linked_href.startswith(skip_url):
                        # If it's a PDF link, append it to the pdf_links list, also add the link title

                        if not linked_a_tag.text or linked_a_tag.text.strip() == '' or linked_a_tag.text.startswith("<"):
                            file_name = os.path.basename(linked_href).replace('_', ' ').replace('-', ' ')
                            pdf_links.append((linked_href, file_name))
                        else:
                            pdf_links.append((linked_href, linked_a_tag.text))  # Save the href and the text from the a tag

                        num_pdf_links += 1
    
    #print(f"Number of total <a> tags found: {num_a_tags}")
    print(f"\n  Number of PDF documents found: {num_pdf_links}")

    # Add "url" before links starting with "/"
    pdf_links = [(link[0][len(base_url):], link[1]) if link[0].startswith(base_url) else link for link in pdf_links]
    
    # Remove duplicate links
    pdf_links = list(set(pdf_links))
    
    # Print number of items in "pdf_links"
    print(f"  Number of normalized PDF links: {len(pdf_links)}")

    return pdf_links
