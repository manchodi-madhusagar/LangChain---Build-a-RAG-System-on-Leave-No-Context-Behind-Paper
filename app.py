from flask import Flask, request, render_template
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
import markdown

app = Flask(__name__)

# Define embedding model
embedding_model = GoogleGenerativeAIEmbeddings(google_api_key="AIzaSyAja8hkFv94G4wz-boAsq8pyEVvd2KtkgQ",
                                               model="models/embedding-001")


# Define Chroma database connection
db_connection = Chroma(persist_directory="chroma_db_", embedding_function=embedding_model)

# Define retriever
retriever = db_connection.as_retriever(search_kwargs={"k": 5})

# Define chat model
chat_model = ChatGoogleGenerativeAI(google_api_key="AIzaSyAja8hkFv94G4wz-boAsq8pyEVvd2KtkgQ",
                                    model="gemini-1.5-pro-latest")

# Define output parser
output_parser = StrOutputParser()

# Define chat template
chat_template = ChatPromptTemplate.from_messages([
    SystemMessage(content="""You are a Helpful AI Bot.
    You take the context and question from the user. Your answer should be based on the specific context."""),
    HumanMessagePromptTemplate.from_template("""Answer the question based on the given context.
    Context:
    {context}

    Question:
    {question}

    Answer: """)
])

# Define RAG chain
rag_chain = (
    {"context": retriever , "question": RunnablePassthrough()}
    | chat_template
    | chat_model
    | output_parser
)

# Define route to handle incoming requests
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = rag_chain.invoke(user_input)
        # Convert response to HTML from Markdown
        response_html = markdown.markdown(response)
        return render_template('index.html', user_input=user_input, response=response_html)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
