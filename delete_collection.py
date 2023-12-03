import chromadb
from chromadb.config import Settings

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

client.delete_collection("livedoor")