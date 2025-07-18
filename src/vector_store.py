from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_openai import OpenAIEmbeddings

from dotenv import load_dotenv
load_dotenv()

class VectorStoreBuilder:
    def __init__(self, csv_path:str, persist_dir:str="chroma_db"):
        self.csv_path = csv_path
        self.persist_dir = persist_dir
        self.embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        
    def build_and_save_vectorstore(self):
        loader = CSVLoader(
            file_path=self.csv_path,
            encoding='utf-8',
            metadata_columns=[]
            
        )
        
        data = loader.load()
        print(f"Loaded {len(data)} documents from CSV")

        splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
        texts = splitter.split_documents(data)

        
        # Create vector store with explicit collection name
        db = Chroma.from_documents(
            texts,
            self.embeddings,
            persist_directory=self.persist_dir
        )

        
    def load_vector_store(self):
        return Chroma(
            persist_directory=self.persist_dir,
            embedding_function=self.embeddings
        )

    
    