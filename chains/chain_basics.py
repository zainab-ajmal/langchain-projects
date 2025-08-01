from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser

#steps:
# 1. creating chat model
# 2. creating prompt template
# 3. create chain
# 4. run the chain and print 

load_dotenv()

model=ChatGroq(model="Llama3-70b-8192")

message=[
    ("system","you are a comedian who tells jokes about {topic}"),
    ("human","tell me {joke_count} jokes."),
]

prompt_template=ChatPromptTemplate.from_messages(message)

#creating combined chain using LangChain using LangChain Expression Language (LECL)
chain = prompt_template | model | StrOutputParser()

result= chain.invoke ({"topic":"laptop","joke_count":2})

print(result)
