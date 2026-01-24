import requests
import wmill


def main():
    """
    Fetch a list of OpenProject IDs from the Django API.

    This function retrieves OpenProject IDs from the Django API by making an
    authenticated GET request. The API URL and the authorization hash are
    fetched as environment variables. It processes the API's JSON response
    to extract the OpenProject IDs of all projects.

    Parameters:
    None

    Raises:
    ValueError: If the response from the API cannot be parsed as JSON, or if the
    expected keys are missing in the response data.

    Returns:
    list: A list of integers or strings containing the OpenProject IDs of all
    projects retrieved from the API.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    r = requests.get(f"{dj_api_url}/projects/", headers=headers)
    return [p.get("openproject_id") for p in r.json()]