import requests
import wmill


def main(work_package_id: int):
    """
    Fetches and returns the ID of a work package from a DataJack API.

    This function retrieves authorization and API URL settings from the Windmill
    variables, constructs an HTTP GET request, and fetches the work package
    details from the provided API. The function then extracts and returns the
    ID from the JSON response.

    Parameters:
    work_package_id (int): The identifier of the work package to fetch.

    Returns:
    int or None: The ID of the work package if found, otherwise None.

    Raises:
    requests.RequestException: If there is an issue with the HTTP request.
    KeyError: If the "id" key is missing in the JSON response.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    url = f"{dj_api_url}/work_packages/{work_package_id}"
    r = requests.get(url, headers=headers)
    return r.json().get("id")