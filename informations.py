import chromadb
from chromadb.config import Settings
import sys

try:
    # Without authentifications
    #client = chromadb.HttpClient(
    #    host='localhost',
    #    port=80)

    # With authentifizations
    client = chromadb.HttpClient(
        host='localhost',
        port=80,
        settings=Settings(chroma_client_auth_provider='chromadb.auth.token.TokenAuthClientProvider',
                          chroma_client_auth_credentials='test-token'))
except Exception as e:
    print('Vector database Connection error occurs with following message.')
    print('Error Message:{0}'.format(str(e)))
    sys.exit(-1)

# discover informations
chroma_heartbeat   = client.heartbeat() 
chroma_version     = client.get_version()
chroma_collections = client.list_collections()

# display informations
print(f'chroma_heartbeat:{chroma_heartbeat}')
print(f'chroma_version  :{chroma_version}')
import pprint
pprint.pprint(chroma_collections,indent=2,width=40)

print(f'chroma_collections[0]  :{chroma_collections[0]}')
# 
collection = client.get_collection("livedoor")

pprint.pprint(collection,indent=2,width=40)

items = collection.get()

#pprint.pprint(items,indent=2,width=40)
#pprint.pprint(items['ids'],indent=2,width=40)
#print('max  ids:{0}'.format(max(items['ids'])))

# display last item
print('last ids:{0}'.format(items['ids'][-1]))
print('last ids:{0}'.format(items['documents'][-1]))
pprint.pprint(items['metadatas'][-1],indent=2,width=40)
