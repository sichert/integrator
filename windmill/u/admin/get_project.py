import requests
import wmill


def main(project_id: int):
    """
    Fetches project information from an external API and returns the project ID.

    This function retrieves project details by making a GET request to an external
    API using the provided project ID. API URL and authorization details are dynamically
    retrieved from predefined variables. The function returns the ID of the project
    as parsed from the API response.

    Args:
        project_id (int): The numeric identifier of the project to fetch.

    Returns:
        int: The project ID extracted from the API response.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    url = f"{dj_api_url}/projects/{project_id}"
    r = requests.get(url, headers=headers)
    return r.json().get("id")