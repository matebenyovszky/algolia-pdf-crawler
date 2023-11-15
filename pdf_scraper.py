import requests
from bs4 import BeautifulSoup

def get_pdf_links(url, websites):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    pdf_links = []
    
    # Find all anchor tags (links) in the page
    num_a_tags = 0
    num_pdf_links = 0

    for a_tag in soup.find_all('a', href=True):
        num_a_tags += 1
        print(f"Number of <a> tags (hyperlinks) found on {url}: {num_a_tags}", end='\r')
        href = a_tag['href']
        
        # Check if the link ends with '.pdf'
        if href.endswith('.pdf'):
            # If it's a PDF link, append it to the pdf_links list
            pdf_links.append(href)
            num_pdf_links += 1
        
        # Check if the link is an internal hyperlink (same domain name)
        elif (url in href) or href.startswith('/'):
           # If it's an internal hyperlink and not "/", scrape the linked HTML page
            if href != '/' and not any(website['url'] in href for website in websites):
                linked_html = requests.get(url + href).content
                linked_soup = BeautifulSoup(linked_html, 'html.parser')
                
                # Find all anchor tags (links) in the linked HTML page
                for linked_a_tag in linked_soup.find_all('a', href=True):
                    linked_href = linked_a_tag['href']
                    
                    # Check if the link ends with '.pdf'
                    if linked_href.endswith('.pdf'):
                        # If it's a PDF link, append it to the pdf_links list
                        pdf_links.append(linked_href)
                        num_pdf_links += 1
    
    print(f"Number of total <a> tags found: {num_a_tags}")
    print(f"Number of PDF documents found: {num_pdf_links}")

    # Add "url" before links starting with "/"
    pdf_links = [url + link if link.startswith("/") else link for link in pdf_links]
    
    # Remove duplicate links
    pdf_links = list(set(pdf_links))
    
    # Remove PDF links that do not start with "url"
    pdf_links = [link for link in pdf_links if link.startswith(url)]

    # Print number of items in "pdf_links"
    print(f"Number of normalized PDF links: {len(pdf_links)}")

    return pdf_links