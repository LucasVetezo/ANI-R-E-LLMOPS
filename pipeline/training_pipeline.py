# This pipeline will be used to build the vector store from the anime dataset

from src.data_ingestion import AnimeDataIngestion
from src.vector_store import VectorStoreBuilder
from dotenv import load_dotenv
from utils.logger import get_logger
from utils.custom_exception import CustomException

load_dotenv()

logger = get_logger(__name__)  # logger initialization using magic method

def main():
    try:
        logger.info("Initializing the training pipeline...")
        
        loader = AnimeDataIngestion("data/anime_with_synopsis.csv","data/anime_updated.csv")
        processed_csv = loader.load_and_process()
        
        logger.info("Data ingestion completed successfully...")
        
        vector_builder = VectorStoreBuilder(processed_csv)
        vector_builder.build_and_save_vectorstore()
        
        logger.info("Vector store built and saved successfully...")
        
        logger.info("Training pipeline completed successfully...")
    except Exception as e:
        logger.error(f"Failed to build the vector store: {e}")
        raise CustomException(f"Error building vector store: {e}")
    
if __name__ == "__main__":
    main()


