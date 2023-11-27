import os

# Initialize the Algolia client with your Application ID and API Key
from algoliasearch.search_client import SearchClient

# Get Algolia API keys from environment variables
algolia_api_key = os.getenv("ALGOLIA_API_KEY")
algolia_app_id = os.getenv("ALGOLIA_APP_ID")
algolia_index_name = os.getenv("ALGOLIA_INDEX_NAME")

client = SearchClient.create('algolia_app_id', 'algolia_api_key')
index = client.init_index('algolia_index_name')


def upload_to_algolia():

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

def is_document_in_index(document_url):
    # Query the Algolia index for the document URL

    # Replace YOUR_APP_ID and YOUR_API_KEY with your Algolia credentials
    #client = SearchClient.create('YOUR_APP_ID', 'YOUR_API_KEY')
    #index = client.init_index('your_index_name')

    # Replace DOCUMENT_URL with the URL of the document you want to check
    document = index.search('', {'filters': 'url:' + document_url})

    if len(document['hits']) > 0:
        print('The document is present in the index database.')
        return True
    else:
        print('The document is not present in the index database.')
        return False
