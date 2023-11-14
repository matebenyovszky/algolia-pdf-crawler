# Add error handling
import logging

def upload_to_algolia(pdf_content):
    try:
        # Read Algolia API key from environment variable
        algolia_api_key = os.environ.get('ALGOLIA_API_KEY')
        
        # Connect to the Algolia index
        client = algoliasearch.Client("YourApplicationID", algolia_api_key)
        index = client.init_index('pdf_content_index')
        
        # Prepare the object to upload
        obj = {
            'content': pdf_content
        }
        
        # Upload the object to the index
        index.save_object(obj)
    except Exception as e:
        logging.error(f'Error occurred while uploading to Algolia: {e}')