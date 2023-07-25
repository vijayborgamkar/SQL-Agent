## Chatbot with Database Integration

#### Overview
This repository contains the codebase for a Language Chain Chatbot that is integrated with various types of databases. The chatbot utilizes the OpenAI GPT-3.5 Turbo language model to answer questions and perform tasks related to the provided databases. The supported database types are MySQL, Oracle, PostgreSQL, Snowflake, and MongoDB.

#### Prerequisites
To use this chatbot, you need to have the following installed:

1. Python (3.6 or higher)
2. psycopg2 (for PostgreSQL)
3. snowflake-connector-python (for Snowflake)
4. cx_Oracle (for Oracle)
5. pymongo (for MongoDB)
6. langchain (custom library, included in the repository)
7. openai

#### Getting Started
- Clone this repository to your local machine.
- Install the required dependencies using pip:

1. Ensure you have an OpenAI API key. If not, sign up for OpenAI and get your API key from the OpenAI website.
2. Update the OPENAI_API_KEY variable in the initialize_chat_agent function with your OpenAI API key.

#### How to Use
1. Run the chatbot script:

`python chatbot.py`

1. The chatbot will prompt you to select a database type (MySQL, Oracle, PostgreSQL, Snowflake, or MongoDB). Type the desired database type or type 'exit' to end the chat.
2. If you selected a supported database type, the chatbot will prompt you to enter the necessary database credentials, such as username, password, host, etc. Enter the required details as prompted or type 'exit' to end the chat.
3. After successfully connecting to the database, you can start asking questions related to the database.
4. Type your questions or queries, and the chatbot will use the OpenAI GPT-3.5 Turbo model and the appropriate database toolkit to provide answers and perform tasks.
5. Type 'exit' at any time to end the chat and exit the program.


#### Supported Database Types
1. MySQL: The chatbot can connect to a MySQL database using the pymysql library.
2. Oracle: The chatbot can connect to an Oracle database using the cx_Oracle library.
3. PostgreSQL: The chatbot can connect to a PostgreSQL database using the psycopg2 library.
4. Snowflake: The chatbot can connect to a Snowflake database using the snowflake-connector-python library.
5. MongoDB: The chatbot can connect to a MongoDB database using the pymongo library.

#### Additional Notes
- The chatbot uses the OpenAI GPT-3.5 Turbo model from the langchain library to generate responses.
- For each database type, the chatbot will prompt you to enter the necessary credentials to establish a connection.
- If an invalid database type is provided, the chatbot will raise a ValueError.
- The chatbot will suppress warnings using the warnings.filterwarnings("ignore") statement.
- Make sure to properly handle sensitive information, such as database credentials, and do not share them publicly.

#### Disclaimer
This chatbot is provided for demonstration purposes and may not be suitable for production use. It is essential to ensure the security and privacy of your data when working with databases and external APIs. Use the chatbot responsibly and in compliance with the terms of service of the services it interacts with.


This project is not officially affiliated with OpenAI or any database providers mentioned. The code is provided as-is without any warranties.
