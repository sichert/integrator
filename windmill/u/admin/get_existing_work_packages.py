import requests
import wmill


def main():
    """
    Retrieves open project IDs for work packages.

    Fetches the list of work packages from a specified API endpoint. The API is
    authenticated using a Basic authorization scheme, where the credentials are
    retrieved from a secure variable storage. The function processes the response
    to extract and return the open project IDs.

    Returns:
        list: A list of open project IDs extracted from the response.

    Raises:
        Any exceptions raised by `requests.get`.

    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    r = requests.get(f"{dj_api_url}/work_packages/", headers=headers)
    return [p.get("openproject_id") for p in r.json()]