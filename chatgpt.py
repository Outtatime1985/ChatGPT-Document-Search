from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import Chroma

def get_answer(question, data_file):
    # Load the text data from the specified file
    loader = TextLoader(data_file)

    # Create a Vectorstore index from the text loader
    index = VectorstoreIndexCreator().from_loaders([loader])

    # Create a Question-Answering chain
    chain = RetrievalQA.from_chain_type(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    # Get the answer from the data based on the provided question
    answer = chain.run(question)

    return answer

# Specify the question/query
question = input("Enter your question: ")
data_file = "data.txt"

# Get the answer from the data
answer = get_answer(question, data_file)

print(answer)
