from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.llms import CTransformers
from langchain.sql_database import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# load_dotenv()

# PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
# PINECONE_API_ENV = os.environ.get('PINECONE_API_ENV')

cs = "mssql+pymssql://username:password@local or remote server URL"
db_engine = create_engine(cs)
db = SQLDatabase(db_engine)
print(db.get_table_names())

llm = CTransformers(
    model="C:\LLM\LLMA2_Chat\End-to-end-PDF-Chatbot-using-Llama2-main\model\llama-2-7b-chat.ggmlv3.q8_0.bin",
    model_type="llama",
    config={"max_new_tokens": 512, "temperature": 0.5},
)
sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
sql_toolkit.get_tools()


# prompt=ChatPromptTemplate.from_messages(
#     [
#         ("system",
#         """
#         you are a very intelligent AI assitasnt who is expert in identifying relevant questions from user and converting into sql queriesa to generate correcrt answer.
#         Please use the below context to write the microsoft sql queries , dont use mysql queries.
#        context:
#        you must query against the connected database, it has total 5 tables , these are Customer,Order,Product,Supplier,OrderItem.
#        Customer table has Id,FirstName,LastName,City,Country,Phone columns.It gives the customer information.
#        Order table has Id,OrderDate,OrderNumber,CustomerId,TotalAmount columns.It gives the order specific information.
#        Product table has Id,ProductName,SupplierId,UnitPrice,Package,IsDiscontinued columns.It gives information about products.
#        Supplier table has Id,CompanyName,ContactName,ContactTitle,City,Country,Phone,Fax columns.This table gives information on the supplier.
#        OrderItem table has Id,OrderId,ProductId,UnitPrice,Quantity columns.It gives information of ordered products.
#        As an expert you must use joins whenever required.
#         """
#         ),
#         ("user","{question}\ ai: ")
#     ]
# )



agent = create_sql_agent(
    llm=llm,
    toolkit=sql_toolkit,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_execution_time=100,
    max_iterations=10,
)
agent.run(
    prompt.format_messages(question="How many rows are avaliable in the Users Table")
)
