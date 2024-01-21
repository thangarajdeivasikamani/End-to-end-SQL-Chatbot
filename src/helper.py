# from langchain.document_loaders.csv_loader  import UnstructuredCSVLoader
# from langchain_community.document_loaders import UnstructuredExcelLoader
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.document_loaders import DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings


#Extract data from the CSV
def load_csv(data):
    loader = DirectoryLoader(data,
                    glob="*.csv",
                    loader_cls=CSVLoader,
                    encoding="utf-8",
                    csv_args={"delimiter": ","}
                    )
    
    documents = loader.load()

    return documents






#download embedding model
def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",model_kwargs = {'device':'cpu'})
    return embeddings