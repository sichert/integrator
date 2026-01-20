import wmill
import requests


def main(x: str):
    """
    Fetches a list of elements from a remote API endpoint.

    This function retrieves data from a specified API URL using a GET
    request. It requires an API endpoint addition to the base URL and
    uses predefined authorization and API URL variables to authenticate
    and construct the request. The response is parsed to extract and
    return the list of elements.

    Parameters:
    x: str
        A string representing the endpoint addition to the base
        API URL.

    Returns:
    list
        A list of elements extracted from the "_embedded" property
        of the JSON response. Returns an empty list if the property
        or elements do not exist.
    """
    authorization_hash = wmill.get_variable("u/admin/op_authorization_hash")
    op_api_url = wmill.get_variable("u/admin/op_api_url")
    r = requests.get(
        f"{op_api_url}{x[1]}",
        headers={
            "Authorization": f"Basic {authorization_hash}"
        },
    )
    return r.json().get("_embedded", {"elements": []}).get("elements", [])
