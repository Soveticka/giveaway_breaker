import graphqlapi
import os
from dotenv import load_dotenv

load_dotenv()

client = graphqlapi.create_client(os.getenv("GRAPHQL_API_URL"))

variables = {"mailbox": "divnoptak", "id":""}

response = graphqlapi.post_query(client, variables, "inbox")

for message in response.get("inbox"):
	print(message.get("id"))