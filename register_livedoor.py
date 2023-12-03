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

# defined sentence transformer LLM
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="intfloat/multilingual-e5-large")

# get or create collection
collection = client.get_or_create_collection("livedoor",embedding_function=sentence_transformer_ef)
collection.add(
    documents=["ある日、スーパーサラリーマンだった“ツレ”が「死にたい！」ってつぶやいた...",
               "今や全国区の人気を誇る“ブサかわ”秋田犬・わさお。今年3月には本人出演による主演映画『わさお』...",
               "芸能界一のリアクション芸人として名高い上島竜兵が、日頃からいじられ続けることに関して不満を持ち"],
    metadatas=[
				{"url": "http://news.livedoor.com/article/detail/5840081/",
         "title": "インタビュー：宮崎あおい＆堺雅人「一緒にいるのが当たり前」",
         "chunk": "1",
         "date": "2011-09-08T10:00:00+0900"},
				{"url": "http://news.livedoor.com/article/detail/5840350/",
         "title": "「さわお」×「わさお」が奇跡の対面",
         "chunk": "1",
         "date": "2011-09-06T16:25:00+0900"},
				{"url": "http://news.livedoor.com/article/detail/5840524/",
         "title": "上島竜兵が「出川には負けない！」と極秘実験でイケメンマッチョに変身",
         "chunk": "1",
         "date": "2011-09-06T17:32:00+0900"}
		],
    ids=["1",
         "2",
         "3"
    ]
)