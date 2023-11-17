import json

def main():
    # Load configuration from config.json
    with open("config.json") as f:
        config = json.load(f)

    pdf_scrape_enabled = config["pdf_scrape_enabled"]
    msdiread_ocr_enabled = config["msdiread_ocr_enabled"]
    upload_enabled = config["upload_enabled"]

    for website in config["websites"]:

        print(f"Website URL: {website["url"]}")
        print(f"Language: {website["language"]}")

        if pdf_scrape_enabled:
            # Search PDF files
            from pdf_scraper import get_pdf_links
            pdf_links = get_pdf_links(website["url"], website["base_url"], website["skip"])
            print("PDF Scrape completed.")

        # Check if PDF-s alre already in the database. If not, go forward
        from algolia import is_document_in_index
        pdf_links = [link for link in pdf_links if not is_document_in_index(link)]
        if not pdf_links:
            continue

        if msdiread_ocr_enabled:
            # OCR PDF files
            from pdf_ocr_msdiread import run_ocr_on_pdf
            scraped_data = run_ocr_on_pdf(pdf_links, website["language"])

        if upload_enabled:
            # Upload data to Algolia
            from algolia import upload_to_algolia
            upload_to_algolia(scraped_data)
            print("Data uploaded to Algolia.")

    print("Crawling completed.")

if __name__ == "__main__":
    main()