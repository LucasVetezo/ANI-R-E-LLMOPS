# To access and load the environment variables inside the project
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY") # assigning a value to the variable OPENAI_API_KEY
MODEL_NAME = "gpt-3.5-turbo"  