#runnable lambda is the custom function that can be plugged into a LangChain pipeline
#runnable sequence is used to define the sequence in which the tasks are to be done, where the output of each is the input of the next.

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.schema.runnable import RunnableLambda, RunnableSequence

load_dotenv()

model=ChatGroq(model="Llama3-70b-8192")

message=[
    ("system","you are a comedian who tells jokes about {topic}"),
    ("human","tell me {joke_count} jokes."),
]
prompt_template = ChatPromptTemplate.from_messages(message)

#creating individual runnables 
first_prompt= RunnableLambda(lambda x: prompt_template.format_prompt(**x)) #**x unpacks the dictionary as keyword arguments.format_prompt(**x) fills the placeholders in the template using values from the input dictionary.
invoke_model = RunnableLambda(lambda x: model.invoke(x.to_messages())) #converts into list of msgs like SystemMessage, HumanMessage, etc.
parse_output = RunnableLambda(lambda x: x.content) #extracts the actual content

#creating runnable sequence
chain = RunnableSequence(first=first_prompt, middle=[invoke_model],last=parse_output) #first & last are single runnable, the middle one is a list

#running the chain
response = chain.invoke({"topic":"chicken","joke_count":2})
print(response)
