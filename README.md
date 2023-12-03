### Algolia PDF Crawler

This repository contains a PDF crawler that extracts text from PDF documents and uploads it to Algolia for indexing and searching.
Currently it uses Microsoft Read model for OCR. Futher development ideas in `.ideas`.

#### Installation

1. Install the required packages by running the following command:

pip install -r requirements.txt

2. Set up the configuration by modifying the `config.json` file. Ensure that the necessary environment variables are defined.

#### Configuration Parameters

The configuration for the PDF crawler is stored in the `config.json` file. The following parameters can be configured:

- `websites`: An array of website objects containing the URL, base URL, and skip settings for each website to be crawled.
- `pdf_scrape_enabled`: A boolean value indicating whether PDF scraping is enabled.
- `msdiread_ocr_enabled`: A boolean value indicating whether OCR using Microsoft Form Recognizer is enabled.
- `upload_enabled`: A boolean value indicating whether the upload to Algolia is enabled.
- `full_crawl`: A boolean value indicating whether a full crawl should be performed.

#### Environment Variables

Ensure that the following environment variables are defined:

- `ALGOLIA_API_KEY`: Your Algolia API key
- `ALGOLIA_APP_ID`: Your Algolia application ID
- `ALGOLIA_INDEX_NAME`: The name of the Algolia index to upload the data to
- `microsoft_di_key`: Your Microsoft Document Intelligence API key
- `microsoft_di_endpoint`: The endpoint for the Microsoft Document Intelligence service

#### Usage

To use the PDF crawler, follow these steps:

1. Install the required packages from `requirements.txt`.
2. Configure the settings in the `config.json` file.
3. Define the necessary environment variables.
4. Run the `main.py` file to start the PDF crawling process.

#### Contributions

Contributions to the PDF crawler are welcome! Submit a pull request with any improvements or bug fixes.

#### License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.