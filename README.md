# ChromaDB client Sample Tools Collection

Welcome to the ChromaDB client sample tools repository.

This repository is a collection of sample client tools for using ChromaDB.
This repository manages a collection of ChromaDB client sample tools for beginners to register the Livedoor corpus with ChromaDB and to perform search testing. Each program assumes that ChromaDB is running on a local PC's port 80 and that ChromaDB is operating with a TokenAuthServerProvider.
Additionally, since the content to be registered with ChromaDB assumes the text format of the Livedoor News corpus, the Livedoor News corpus is required for operation.

## Included Sample Tools

The collection includes the following tools:

- **register_livedoor.py**: Illustrates how to interact with the ChromaDB API.
- **informations.py**: Illustrates how to interact with the ChromaDB API.
- **indexing_livedoor.py**: Provides a template for creating visualizations from ChromaDB data.
- **query_livedoor.py**: Demonstrates the process of importing and exporting data to and from ChromaDB.
- **delete_collection.py**: Provides a template for creating visualizations from ChromaDB data.

## Installation

To begin using these sample tools, first clone the repository or download its contents to your local system.

**1.Git Clone**: 
Clone from GitHub repository.
```bash
git clone https://github.com/potofo/chromadb_client.git
```
**2.Create Virtual Environment for Python**
```bash
cd chromadb_client
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

**3.Activate Virtual Environment for Python**
```bash
venv\Scripts\activate.bat
pip install -r requirements.txt
```

**4.pip install**
```bash
pip install -r requirements.txt
```



## Usage

Each sample tool comes with usage guidelines. For detailed instructions on how to use a specific tool, check the `README.md` file located in the tool's own directory.

**1.Create Virtual Environment for Python.**
Create a Python virtual environment (venv) with the following command.
```
mkdir chromadb
cd chromadb
python -m venv venv
```
**2.Start Chromadb in server mode.**
Here, will use TokenAuthServerProvider to configure token authentication with the name "test-token".
```
REM start.bat
call "venv\Scripts\activate.bat"
SET CHROMA_SERVER_AUTH_CREDENTIALS=
SET CHROMA_SERVER_AUTH_CREDENTIALS_PROVIDER=
SET CHROMA_SERVER_AUTH_PROVIDER=

SET CHROMA_SERVER_AUTH_CREDENTIALS=test-token
SET CHROMA_SERVER_AUTH_CREDENTIALS_PROVIDER=chromadb.auth.token.TokenConfigServerAuthCredentialsProvider
SET CHROMA_SERVER_AUTH_PROVIDER=chromadb.auth.token.TokenAuthServerProvider

chroma run --path db --port 80

```
**3.Try informations.py Run**
There will be an error the first time because there is no collection named livedoor, but if chroma_version is displayed it will be successful.
```
(venv) Q:\OneDrive\Python\chromadb_client>python informations.py
chroma_heartbeat:1701592099729834400
chroma_version  :0.4.17
[]
chroma_collections[0]  :name='livedoor_master' id=UUID('d2629131-05c5-4d98-b514-168bb51aa94e') metadata={'hnsw:space': 'cosine'} tenant='default_tenant' database='default_database'
Traceback (most recent call last):
  File "Q:\OneDrive\Python\chromadb_client\venv\lib\site-packages\chromadb\api\fastapi.py", line 628, in raise_chroma_error
    resp.raise_for_status()
  File "Q:\OneDrive\Python\chromadb_client\venv\lib\site-packages\requests\models.py", line 1021, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: http://localhost:80/api/v1/collections/livedoor1?tenant=default_tenant&database=default_database

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "Q:\OneDrive\Python\chromadb_client\informations.py", line 35, in <module>
    collection = client.get_collection("livedoor1")
  File "Q:\OneDrive\Python\chromadb_client\venv\lib\site-packages\chromadb\api\client.py", line 207, in get_collection
    return self._server.get_collection(
  File "Q:\OneDrive\Python\chromadb_client\venv\lib\site-packages\chromadb\telemetry\opentelemetry\__init__.py", line 127, in wrapper
    return f(*args, **kwargs)
  File "Q:\OneDrive\Python\chromadb_client\venv\lib\site-packages\chromadb\api\fastapi.py", line 280, in get_collection
    raise_chroma_error(resp)
  File "Q:\OneDrive\Python\chromadb_client\venv\lib\site-packages\chromadb\api\fastapi.py", line 630, in raise_chroma_error
    raise (Exception(resp.text))
Exception: {"error":"ValueError('Collection livedoor1 does not exist.')"}
```

**4.download live door news corpus**
Download ldcc-20140209.tar.gz from the URL below and place it in the path of the directory variable in the indexing_livedoor.py code.

https://www.rondhuit.com/download.html


**5.register livedoor news corpus**
Run indexing_livedoor.py code to register 870 livedoor news corpus

**6.ReTry informations.py Run**

**7.Try query_livedoor.py Run**


## Dependencies

Some sample tools may require external libraries or software to function correctly. Required dependencies will be listed in the respective `requirements.txt` files or inside the tool's documentation.

```bash
pip install -r requirements.txt  # Install required Python dependencies
```

## Contributing

We welcome contributions that enhance the functionality of our sample tools or introduce new features relevant to the ChromaDB community. If you have improvements or bug fixes, please submit pull requests with detailed descriptions of your updates, ensuring compatibility with the existing codebase.

## License

The sample tools in this collection are provided under the [MIT License](LICENSE), unless specified otherwise alongside the tool's resources.

## Support

For questions or issues regarding these sample tools, please utilize the issue tracking system provided by the repository hosting platform.

---

We hope you find the ChromaDB Sample Tools Collection valuable for your projects, and we look forward to seeing what creative solutions you develop with these resources!