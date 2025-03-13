from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

def create_client(url: str) -> Client:
    """
    Creates a GraphQL client using the provided URL.
    Args:
        url (str): The URL of the GraphQL endpoint.
    Returns:
        Client: A GraphQL client configured with the specified URL.
    """
    transport = RequestsHTTPTransport(url=url)
    client = Client(transport=transport, fetch_schema_from_transport=True)
    return client

def post_query(client: Client,variables: dict[str, str], queryReturn: str) -> dict:
    """ Function to post a query to the graphql API

    Args:
        variables (dict[str, str]): Dictionary with variables for the query in format {"variable": "value"}. Mandatory variable is "mailbox". If you want to get a specific message, you need to provide "id" as well.
        queryReturn (str): String with the name of the query to return. Possible values are "message", "inbox" and "delete".

    Returns:
        dict: Response from the API in dictionary format.
    """ 
    if queryReturn == "inbox":
        query = gql(f"""query Example($mailbox: String!) {{{queryReturn}(mailbox: $mailbox) {{id headerfrom subject date html}}}}""")
    else:
        query = gql(f"""query Example($mailbox: String!, $id: String!) {{{queryReturn}(mailbox: $mailbox, id: $id) {{id headerfrom subject date html}}}}""")

    response = client.execute(query, variable_values=variables)
    return response