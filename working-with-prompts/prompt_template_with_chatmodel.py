from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage

load_dotenv()

#in this file, along with creating the prompt we will actually pass it to the LLM to get the result.

model=ChatGroq(model="Llama3-70b-8192")

messages = [
    ("system","you are a comedian who tells joke about {topic}"),
    (HumanMessage(content="tell 3 jokes")),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"cats"})
result=model.invoke(prompt)
print(result.content)

