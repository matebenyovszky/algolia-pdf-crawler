import json
import datetime

# Initialize the Algolia client with your Application ID and API Key
import os
from algoliasearch.search_client import SearchClient

# Get Algolia API keys from environment variables
algolia_api_key = os.getenv("ALGOLIA_API_KEY")
algolia_app_id = os.getenv("ALGOLIA_APP_ID")
algolia_index_name = os.getenv("ALGOLIA_INDEX_NAME")

# Create client
client = SearchClient.create(algolia_app_id, algolia_api_key)
index = client.init_index(algolia_index_name)

def main():
    # Load configuration from config.json
    with open("config.json") as f:
        config = json.load(f)

    print(str(datetime.datetime.now()) + " Crawling started")

    if config["upload_enabled"]:


        if config["full_crawl"]:
            # Delete all PDFs from the index
            from algolia import delete_all_pdf
            delete_all_pdf(index)
        else:
            pass      

    for website in config["websites"]:
        # Print website URL and language
        print(f" Website URL: {website['url']}")
        print(f" Language: {website['language']}")

        if config["pdf_scrape_enabled"]:
            # Search for PDF files
            from pdf_scraper import get_pdf_links
            pdf_links = get_pdf_links(website["url"], website["base_url"], website["skip"])
            print(str(datetime.datetime.now()) + " PDF collection completed")

        if config["upload_enabled"]:
            if not config["full_crawl"]:
                from algolia import is_document_in_index
                pdf_links = [link for link in pdf_links if not is_document_in_index(link[0], index)]
                if not pdf_links:
                    continue
            #else:
                #continue

        if config["msdiread_ocr_enabled"]:
            # Check if file has a text layer already from pdf_text_layer should be implenented

            # OCR PDF files
            from pdf_ocr_msdiread import run_ocr_on_pdf
            scraped_data = run_ocr_on_pdf(pdf_links, website["language"], website["base_url"])

        if config["upload_enabled"]:
            # Upload data to Algolia
            from algolia import upload_to_algolia
            upload_to_algolia(scraped_data, index)
            print(str(datetime.datetime.now()) + " Algolia index updated")

    print(str(datetime.datetime.now()) + " Crawling completed.")

if __name__ == "__main__":
    main()