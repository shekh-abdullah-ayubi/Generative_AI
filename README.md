Steps to be followed in RAG implementation setup -
* `uv init` - to initilize the project.
* `uv venv` - to create virtual environment for project.
* `.venv\Scripts\activate` - Activate virtual environment.
* `uv add -r .\requirements.txt` - Install required modules.

Architecture :- 
Data Ingestion -> Dividing into Chunks using text splitter -> Embed  text to vector -> Store in VectorStore DB -> perform query -> embed query -> generate context + Prompt -> LLM -> Output 

/src/ -> __init__.py -> data_loader.py -> embedding.py -> vectorstore.py -> search.py 