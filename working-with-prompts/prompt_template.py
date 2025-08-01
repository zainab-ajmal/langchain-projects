from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage


#here, it will just create the message in the prompt like structure
#ChatPromptTemplate.from_messages() is a convenient method in LangChain that helps you create a structured prompt for chat-based models

#prompt expects a tuple (when string manipulation is used) where you tell the message type first followed by the content
# messages= [
#     ("system", "you are a comedian whole tells jokes about {topic}."),
#     ("human", "tell me {jokes_count} jokes"),
# ]

# prompt_template= ChatPromptTemplate.from_messages(messages)
# prompt= prompt_template.invoke({"topic":"cats", "jokes_count":3})
# print(prompt)

#when there is no string manipulation we dont have to write it as tuple (e.g. see the difference bw the both human messages)
messages = [
    ("system","you are a comedian who tells joke about {topic}"),
    (HumanMessage(content="tell 3 jokes")),
]
prompt_template = ChatPromptTemplate.from_messages(messages)
prompt = prompt_template.invoke({"topic":"cats"})
print(prompt)


# # PART 2: Prompt with Multiple Placeholders
# print("\n----- Prompt with Multiple Placeholders -----\n")
# template_multiple = """You are a helpful assistant.
# Human: Tell me a {adjective} short story about a {animal}.
# Assistant:"""
# prompt_multiple = ChatPromptTemplate.from_template(template_multiple)
# prompt = prompt_multiple.invoke({"adjective": "funny", "animal": "panda"})
# print(prompt)

