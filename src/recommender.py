from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI 
from src.prompt_template import get_anime_prompt

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatOpenAI(api_key=api_key, model=model_name, temperature=0)
        self.prompt = get_anime_prompt()
        self.qa_chain = RetrievalQA.from_llm(
            llm=self.llm,
            retriever=retriever,
            return_source_documents=True,
            prompt=self.prompt
        )
    
    def get_recommendation(self, query: str):
        result = self.qa_chain({"query": query})
        return result['result']