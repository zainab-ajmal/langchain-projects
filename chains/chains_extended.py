from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model=ChatGroq(model="Llama3-70b-8192")

message=[
    ("system","you are a comedian who tells jokes about {topic}"),
    ("human","tell me {joke_count} jokes."),
]

prompt_template=ChatPromptTemplate.from_messages(message)

#adding the aditional tasks (runnable lambdas) for counting the number of words and covnerting the output to uppercase

uppercase_output = RunnableLambda(lambda x: x.upper())
count_words =  RunnableLambda(lambda x: f"the word count is {len(x.split())}\n{x}")

#LECL
chain = prompt_template | model | StrOutputParser() | uppercase_output | count_words 

result= chain.invoke({"topic":"pen","joke_count":1})
print(result)