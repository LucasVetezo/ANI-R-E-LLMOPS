# This pipeline will be used to generate responses based on user queries

from ast import main
from src.vector_store import VectorStoreBuilder
from src.recommender import AnimeRecommender
from config.config import OPENAI_API_KEY, MODEL_NAME
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)                           # logger initialization using magic method

class AnimeRecommendationPipeline:
    def __init__(self,persist_dir="chroma_db"):
        try:
            logger.info("Initializing recommendation pipeline")
            logger.info("Initializing vector store...")
            
            vector_builder = VectorStoreBuilder(csv_path="", persist_dir=persist_dir)       # We are just loading the vector store
            
            retriever = vector_builder.load_vector_store().as_retriever()  # Load the vector store as retriever

            self.recommender = AnimeRecommender(retriever, OPENAI_API_KEY, MODEL_NAME)

            logger.info("Recommendation pipeline initialized successfully...")
            
        except Exception as e:
            logger.error(f"Failed to initialize recommendation pipeline: {e}")
            raise CustomException(f"Error initializing recommendation pipeline: {e}")
        
    def recommend(self, query:str)-> str:
        try:
            logger.info(f"Received a query: {query}")
            
            recommendation = self.recommender.get_recommendation(query)  # Get recommendation from the recommender
            
            logger.info("Recommendation generated successfully...")
            return recommendation
        except Exception as e:
            logger.error(f"Failed to get recommendation: {e}")
            raise CustomException(f"Error getting recommendation: {e}")
        
