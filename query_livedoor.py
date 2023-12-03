import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

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

sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="intfloat/multilingual-e5-large")

try:
    collection = client.get_collection(name="livedoor", embedding_function=sentence_transformer_ef)
except Exception as e:
    print(e)


#prompt = "宮崎あおい"
#prompt = "ヴェネチア国際映画祭で金獅子賞を受賞した映画はなんですか？"
#prompt = "兎が出てくるホラー映画はなんですか？"
prompt = "映画三銃士の主演女優の名前を教えてください。"

results = collection.query(
     query_texts=prompt,
     n_results=3,
     #include=['documents', 'distances', 'metadatas','embeddings']
     include=['documents', 'distances', 'metadatas']
)

print(results['ids'])
print(results['distances'])
print(results['documents'])
print(results['metadatas'])

