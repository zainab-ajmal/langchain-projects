from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.schema import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model= ChatGroq(model="Llama3-70b-8192")

chat_history=[] #list for storing messages

system_message= SystemMessage(content="You are an AI assistant and your goal is to help users solve their questions and problems clearly, efficiently, and cheerfully.")
chat_history.append(system_message) #appending system message to chat history

#chat loop
while True:
    query= input("You:")
    if query.lower() == "exit":
        break
    chat_history.append(HumanMessage(content=query)) #add the user query in the chat history

    #invoking the model for the AI response
    result=model.invoke(chat_history)
    response = result.content
    chat_history.append(AIMessage(content=response)) #add the AI response in teh chat history
    print("AI's response:", response)


#print("---- Message History--- ")
#print(chat_history)