import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize the Algolia client with your Application ID and API Key
from algoliasearch.search_client import SearchClient

def upload_to_algolia():

    # Get Algolia API keys from environment variables
    algolia_api_key = os.getenv("ALGOLIA_API_KEY")
    algolia_app_id = os.getenv("ALGOLIA_APP_ID")
    algolia_index_name = os.getenv("ALGOLIA_INDEX_NAME")

    # Inicializálj egy Algolia kereső klienst
    client = SearchClient.create(algolia_app_id, algolia_api_key)

    # Select the index you want to upload data to
    # Inicializálj egy Algolia kereső klienst
    client = SearchClient.create(algolia_app_id, algolia_api_key)

    # Select the index you want to upload data to
    index = client.init_index(algolia_index_name)

    # Az feltölteni kívánt objektumok
    objects_to_upload = [
        {
            'objectID': '1',
            'title': 'Sample Title 1',
            'content': 'Sample Content 1',
            'language': 'English',
            'excerpt': 'Sample excerpt 1',
            'path': '/sample-path-1'
        },
        {
            'objectID': '2',
            'title': 'Sample Title 2',
            'content': 'Sample Content 2',
            'language': 'Spanish',
            'excerpt': 'Sample excerpt 2',
            'path': '/sample-path-2'
        }
    ]

    # Upload the object to Algolia
    try:
        response = index.save_objects(objects_to_upload)
        print("Upload successful:", response)
    except Exception as e:
        print("An error occurred:", e)