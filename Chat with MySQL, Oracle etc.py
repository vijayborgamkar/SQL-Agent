from langchain.agents import load_tools, initialize_agent, AgentType, AgentExecutor
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.agents import create_sql_agent
from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain.chat_models import ChatOpenAI
import os
import psycopg2
import snowflake.connector
from pymongo import MongoClient
import cx_Oracle
import warnings
warnings.filterwarnings("ignore")


def initialize_chat_agent(db_type, db_credentials=None):
    os.environ['OPENAI_API_KEY'] = "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"

    if db_type == 'mysql':
        db_user = input("Enter the MySQL database user: ")
        if db_user.lower() == 'exit':
            return None

        db_password = input("Enter the MySQL database password: ")
        if db_password.lower() == 'exit':
            return None

        db_host = input("Enter the MySQL database host: ")
        if db_host.lower() == 'exit':
            return None

        db_name = input("Enter the MySQL database name: ")
        if db_name.lower() == 'exit':
            return None

        db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}")

    elif db_type == 'oracle':
        db_user = input("Enter the Oracle database user: ")
        if db_user.lower() == 'exit':
            return None

        db_password = input("Enter the Oracle database password: ")
        if db_password.lower() == 'exit':
            return None

        db_host = input("Enter the Oracle database host: ")
        if db_host.lower() == 'exit':
            return None

        db_sid = input("Enter the Oracle database SID: ")
        if db_sid.lower() == 'exit':
            return None

        dsn = cx_Oracle.makedsn(host=db_host, sid=db_sid)
        db = cx_Oracle.connect(user=db_user, password=db_password, dsn=dsn)

    elif db_type == 'postgres':
        db_user = input("Enter the PostgreSQL database user: ")
        if db_user.lower() == 'exit':
            return None

        db_password = input("Enter the PostgreSQL database password: ")
        if db_password.lower() == 'exit':
            return None

        db_host = input("Enter the PostgreSQL database host: ")
        if db_host.lower() == 'exit':
            return None

        db_port = input("Enter the PostgreSQL database port: ")
        if db_port.lower() == 'exit':
            return None

        db_name = input("Enter the PostgreSQL database name: ")
        if db_name.lower() == 'exit':
            return None

        dsn = f"host={db_host} port={db_port} dbname={db_name} user={db_user} password={db_password}"
        db = psycopg2.connect(dsn)

    elif db_type == 'snowflake':
        account = input("Enter the Snowflake account name: ")
        if account.lower() == 'exit':
            return None

        user = input("Enter the Snowflake user name: ")
        if user.lower() == 'exit':
            return None

        password = input("Enter the Snowflake password: ")
        if password.lower() == 'exit':
            return None

        warehouse = input("Enter the Snowflake warehouse name: ")
        if warehouse.lower() == 'exit':
            return None

        database = input("Enter the Snowflake database name: ")
        if database.lower() == 'exit':
            return None

        schema = input("Enter the Snowflake schema name: ")
        if schema.lower() == 'exit':
            return None

        db = snowflake.connector.connect(
            account=account,
            user=user,
            password=password,
            warehouse=warehouse,
            database=database,
            schema=schema
        )

    elif db_type == 'mongodb':
        db_host = input("Enter the MongoDB host: ")
        if db_host.lower() == 'exit':
            return None

        db_port = input("Enter the MongoDB port: ")
        if db_port.lower() == 'exit':
            return None

        db_user = input("Enter the MongoDB user: ")
        if db_user.lower() == 'exit':
            return None

        db_password = input("Enter the MongoDB password: ")
        if db_password.lower() == 'exit':
            return None

        db_name = input("Enter the MongoDB database name: ")
        if db_name.lower() == 'exit':
            return None

        client = MongoClient(f"mongodb://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}")
        db = client[db_name]

    else:
        raise ValueError("Invalid database type.")

    llm = ChatOpenAI(model_name="gpt-3.5-turbo")

    toolkit = SQLDatabaseToolkit(db=db)
    agent_executor = create_sql_agent(llm=llm, toolkit=toolkit, verbose=True)

    return agent_executor


def ask_agent_question(agent_executor, question):
    try:
        response = agent_executor.run(question)
        return response
    except Exception as e:
        print("Error occurred during question execution:", str(e))
        return "The answer was not found. Please enter the question with more details."


def chat_loop():
    while True:
        db_type = input("Select a database type (mysql, oracle, postgres, snowflake, mongodb) (Type 'exit' to end): ")
        if db_type.lower() == 'exit':
            print("Exiting...")
            break

        if db_type.lower() not in ['mysql', 'oracle', 'postgres', 'snowflake', 'mongodb']:
            print("Invalid database type. Please try again.")
            continue

        agent = initialize_chat_agent(db_type)
        if agent is None:
            print("Exiting...")
            break

        while True:
            user_input = input("What would you like to know? (Type 'exit' to end): ")
            if user_input.lower() == 'exit':
                print("Exiting...")
                break

            response = ask_agent_question(agent, user_input)
            print(response)

        print()


# Start the chat loop
chat_loop()