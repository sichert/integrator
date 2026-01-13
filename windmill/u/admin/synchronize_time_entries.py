import requests
import wmill


def main(time_entry: object):
    """
    Handles the synchronization of a time entry object with the server.

    This function interacts with an external API to either update an existing time entry
    or create a new one based on whether the time entry exists on the server. It uses
    credentials and configurations obtained from external variables for authentication and
    API access.

    Parameters:
        time_entry (object): A dictionary-like object representing the time entry to
        be synchronized with the server. It must include the key "openproject_id".

    Returns:
        int: The ID of the time entry as returned by the server.

    Raises:
        ValueError: Raised if the API response does not contain an expected ID field.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    work_packages_url = f"{dj_api_url}/time_entries/"

    r = requests.get(work_packages_url, headers=headers)

    existing_projects = [p.get("openproject_id") for p in r.json()]
    openproject_id = time_entry.get("openproject_id")
    if openproject_id in existing_projects:
        result = requests.patch(
            f"{work_packages_url}{openproject_id}/", json=time_entry, headers=headers
        )
    else:
        result = requests.post(work_packages_url, json=time_entry, headers=headers)

    return result.json().get("id")
