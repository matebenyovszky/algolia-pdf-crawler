import json
from datetime import datetime

# /algolia-pdf-crawler/.venv/Scripts/Activate.ps1

def main():
    # Load configuration from config.json
    with open("config.json") as f:
        config = json.load(f)

    pdf_scrape_enabled = config["pdf_scrape_enabled"]
    msdiread_ocr_enabled = config["msdiread_ocr_enabled"]
    upload_enabled = config["upload_enabled"]

    for website in config["websites"]:
        website_url = website["url"]
        website_base_url = website["base_url"]
        language = website["language"]
        skip_url = website["skip"]

        print(f"Website URL: {website_url}")
        print(f"Language: {language}")

        if pdf_scrape_enabled:
            # PDF files
            from pdf_scraper import get_pdf_links
            pdf_links = get_pdf_links(website_url, website["base_url"], skip_url)
            print("PDF Scrape completed.")

        if msdiread_ocr_enabled:
            from pdf_ocr_msdiread import run_ocr_on_pdf
            scraped_data = run_ocr_on_pdf(pdf_links)
            scraped_data["language"] = language
            scraped_data["url"] = pdf_links

        if upload_enabled:
            # Upload data to Algolia
            from algolia_upload import upload_to_algolia
            upload_to_algolia(scraped_data)
            print("Data uploaded to Algolia.")

    print("Crawling completed.")

if __name__ == "__main__":
    main()