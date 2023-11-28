import os

# Initialize the Algolia client with your Application ID and API Key
from algoliasearch.search_client import SearchClient

# Get Algolia API keys from environment variables
algolia_api_key = os.getenv("ALGOLIA_API_KEY")
algolia_app_id = os.getenv("ALGOLIA_APP_ID")
algolia_index_name = os.getenv("ALGOLIA_INDEX_NAME")

#Create client
client = SearchClient.create(algolia_app_id, algolia_api_key)
index = client.init_index(algolia_index_name)


def upload_to_algolia(objects_to_upload):

    # Az feltölteni kívánt objektumok
    # objects_to_upload = [
    #     {
    #         'objectID': '1',
    #         'title': 'Sample Title 1',
    #         'content': 'Sample Content 1',
    #         'language': 'en',
    #         'excerpt': 'Sample excerpt 1',
    #         'path': '/sample-path-1'
    #     },
    #     {
    #         'objectID': '2',
    #         'title': 'Sample Title 2',
    #         'content': 'Sample Content 2',
    #         'language': 'en',
    #         'excerpt': 'Sample excerpt 2',
    #         'path': '/sample-path-2'
    #     }
    # ]

    # Upload the object to Algolia
    try:
        response = index.save_objects(objects_to_upload)
        print("Upload successful:", response)
    except Exception as e:
        print("An error occurred:", e)

def is_document_in_index(document_url):
    # Query the Algolia index for the document URL

    # Useful doc:
    # https://www.algolia.com/doc/api-reference/search-api-parameters/
    # https://www.algolia.com/doc/api-reference/api-parameters/filters/ 
    #document = index.search(document_url, {'attributesToRetrieve': ['path', 'language'], 'filters': "language:'hu'", 'hitsPerPage': 50})

    #Assuming language is not relevant:
    document = index.search(document_url, {'attributesToRetrieve': ['path', 'language']})

    if len(document['hits']) > 0:
        print('The document is present in the index database.')
        return True
    else:
        print('The document is not present in the index database.')
        return False

def delete_all_pdf(index):
    # https://www.algolia.com/doc/api-reference/api-methods/delete-by/
    response = index.delete_by({
      'filters': "path:'.pdf'"})
    print('*.pdf deleted from index')
    