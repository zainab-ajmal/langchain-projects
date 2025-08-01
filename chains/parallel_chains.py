from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain.schema.runnable import RunnableLambda, RunnableParallel
from langchain.schema.output_parser import StrOutputParser

load_dotenv()

model=ChatGroq(model="Llama3-70b-8192")

# Define prompt template
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an expert product reviewer."),
        ("human", "List the main features of the product {product_name}."),
    ]
)


# Define pros analysis step
def analyze_pros(features):
    pros_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human","Given these features: {features}, list the pros of these features.",
            ),
        ]
    )
    return pros_template.format_prompt(features=features)


# Define cons analysis step
def analyze_cons(features):
    cons_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are an expert product reviewer."),
            (
                "human", "Given these features: {features}, list the cons of these features.",
            ),
        ]
    )
    return cons_template.format_prompt(features=features)

def combine_pros_cons(pros,cons):
    return f"Pros:\n{pros}\n\nCons:{cons}"
#simplifying branches wusing LECL
pros_branch_chain = (
    RunnableLambda(lambda x: analyze_pros(x)) | model| StrOutputParser ()
)
cons_branch_chain = (
    RunnableLambda (lambda x: analyze_cons(x)) |model| StrOutputParser ()
)
#combine both branches
combine_branches = RunnableLambda(lambda x : combine_pros_cons(x["branches"]["pros"],x["branches"]["cons"]))

chain=(
    prompt_template
    | model
    | StrOutputParser ()
    | RunnableParallel(branches={"pros":pros_branch_chain,"cons":cons_branch_chain})
    | combine_branches
)

result =  chain.invoke({"product_name":"Xiaomi 13 pro"})

print(result)