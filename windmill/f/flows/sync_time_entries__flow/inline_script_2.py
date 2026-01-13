import wmill
import requests


def main(x: str):
    """
    Executes a GET request to a specified API endpoint and retrieves entity data.

    The function retrieves authentication details and API URL from a secure source,
    performs a GET request using the provided input as an endpoint, and extracts
    the 'entity' data from the response.

    Parameters:
    x (str): The endpoint to append to the API URL.

    Returns:
    dict: A dictionary containing the 'entity' data retrieved from the API response.
    """
    authorization_hash = wmill.get_variable("u/admin/op_authorization_hash")
    op_api_url = wmill.get_variable("u/admin/op_api_url")
    r = requests.get(
        f"{op_api_url}{x}",
        headers={
            "Authorization": f"Basic {authorization_hash}"
        },
    )
    return r.json()
