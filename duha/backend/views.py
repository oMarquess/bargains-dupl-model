from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from .config import OPENAI_API_KEY, llm
from .db_setup import db



class QueryView(APIView):
    """
    View to handle queries. Returns true if the product is already in the database and false if no such product is available
    """
    permission_classes = [permissions.AllowAny]
   

    def post(self, request, format=None):
        
         # Define the QA template
        template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Don't answer any question outside of pieces of context, say it's out of context.
        Do we have exactly this {question} in the product list? If no, say False, If yes say True.
        {context}
        Question: {question}
        Helpful Answer:
        """  # Your existing template
        QA_CHAIN_PROMPT = PromptTemplate.from_template(template)
        memory = ConversationBufferMemory(
                memory_key="chat_history",
                return_messages=True
                )
        # Create the retriever and RQA chain
        retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 4})
        rqa = RetrievalQA.from_chain_type(llm,
                                          chain_type="stuff",
                                          retriever=retriever,
                                          chain_type_kwargs={"prompt": QA_CHAIN_PROMPT},
                                          memory=memory,
                                          #return_source_documents=True
                                          )

        # Get the query from the request
        query = request.data.get('query', '')

        if query:
            # Process the query
            result = rqa(query)['result']
            return Response({'result': result}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No query provided'}, status=status.HTTP_400_BAD_REQUEST)


