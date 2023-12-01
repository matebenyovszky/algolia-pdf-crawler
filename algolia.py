    # Useful doc:
    # https://www.algolia.com/doc/api-reference/search-api-parameters/
    # https://www.algolia.com/doc/api-reference/api-parameters/filters/ 

def upload_to_algolia(objects_to_upload, index):

    # Upload the object to Algolia
    try:
        response = index.save_objects(objects_to_upload)
        print("Upload successful:", response)
    except Exception as e:
        print("An error occurred:", e)

def is_document_in_index(document_url, index):
    # Query the Algolia index for the document URL

    #Assuming language is not relevant:
    document = index.search(document_url, {'attributesToRetrieve': ['path', 'language']})

    # response = index.search('',{'filters': 'language:"en"'}) - if language is relevant... should be added next versions - lang field should be crawled
    #document = index.search(document_url, {'attributesToRetrieve': ['path', 'language'], 'filters': "language:'hu'", 'hitsPerPage': 50})

    if len(document['hits']) > 0:
        print('The document is present in the index database.')
        return True
    else:
        print('The document is not present in the index database.')
        return False

def delete_all_pdf(index):

    # https://www.algolia.com/doc/api-reference/api-methods/delete-by/
    index.delete_by({'filters': 'type:"pdf"'})

    return('*.pdf deleted from index')
    
