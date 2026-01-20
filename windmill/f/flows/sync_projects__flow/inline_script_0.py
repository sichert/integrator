import wmill
import requests


def main():
    """
    Fetches the list of projects from the specified API endpoint.

    This function retrieves project information by sending an HTTP GET request to
    the OpenProject API endpoint. Authorization for the request is handled
    using a hashed token obtained through configuration variables. The request URL
    and the authorization hash are both dynamically fetched from environment
    variables.

    Returns
    -------
    list
        A list of project elements retrieved from the API response. If the response
        does not contain the expected data structure, an empty list is returned.

    Raises
    ------
    requests.RequestException
        If an issue occurs while making the HTTP request.
    """
    authorization_hash = wmill.get_variable("u/admin/op_authorization_hash")
    op_api_url = wmill.get_variable("u/admin/op_api_url")
    r = requests.get(
        f"{op_api_url}/api/v3/projects",
        headers={
            "Authorization": f"Basic {authorization_hash}"
        },
    )
    return r.json().get("_embedded", {"elements": []}).get("elements", [])
