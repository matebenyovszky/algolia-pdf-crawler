import threading
import time
from spinner import spinner_task

# Load existing code with spinner

def main():
    # Load configuration from config.json
    with open("config.json") as f:
        config = json.load(f)

    pdf_scrape_enabled = config["pdf_scrape_enabled"]
    upload_enabled = config["upload_enabled"]

    for website in config["websites"]:
        website_url = website["url"]
        language = website["language"]

        print(f"Website URL: {website_url}")
        print(f"Language: {language}")

        if pdf_scrape_enabled:
            # PDF files
            from pdf_scraper import get_pdf_links
            pdf_links = get_pdf_links(website_url, config["websites"])
            print("PDF Scrape completed.")

            from pdf_ocr import run_ocr_on_pdf
            scraped_data = run_ocr_on_pdf(pdf_links)
            scraped_data["language"] = language

        if upload_enabled:
            # Upload data to Algolia
            threading.Thread(target=spinner_task).start()
            from algolia_upload import upload_to_algolia
            upload_to_algolia(scraped_data)
            print("Data uploaded to Algolia.")

    print("Crawling completed.")

if __name__ == "__main__":
    main()