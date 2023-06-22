# ChatGPT-Insights Search based on Documents
![image](https://github.com/Outtatime1985/ChatGPT-Document-Search/assets/54365436/96fb162b-55ed-413a-a56c-52aae44a3482)


## Description
This project utilizes the LangChain library to provide a question-answering functionality based on a specified text data file. It incorporates the following components:

- **RetrievalQA**: A question-answering chain that utilizes language models and vector stores for information retrieval.
- **ChatOpenAI**: A chat-based language model (specifically, "gpt-3.5-turbo") used for generating responses.
- **TextLoader**: A text data loader used to load the specified data file.
- **VectorstoreIndexCreator**: A creator class for generating a vector store index from text loaders.
- **Chroma**: A vector store implementation used for indexing and retrieving data.

The purpose of this project is to enable users to input a question/query and obtain an answer based on the provided text data file. The LangChain library is employed to perform efficient information retrieval and provide accurate responses.

## Installation
Follow the instructions below to set up and run the project on your local machine.

### Prerequisites
- Python (version X.X.X or higher)
- Pip package manager

### Installation Steps
1. Clone the repository: `git clone https://github.com/your-username/project.git`
2. Navigate to the project directory: `cd project`
3. Install the required dependencies:
   - `pip install langchain`
   - `pip install openai`
   - `pip install chromadb`
   - `pip install tiktoken`
   (Replace `langchain` with the appropriate package name if available)

## Usage
1. Ensure that you have prepared a text data file containing the information you want to query.
2. Open the code file containing the provided code snippet.
3. Locate the `data_file` variable and update it with the path to your data file.
4. Run the script.
5. When prompted, enter your question/query.
6. The program will use the LangChain library to retrieve the answer from the specified data based on your question/query and display it.

