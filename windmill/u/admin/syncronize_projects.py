import json

import requests
import wmill


def main(
    project: object
):
    """
    Main function for synchronizing a project object with a remote API.
    This function serializes the given project, retrieves necessary API
    credentials, and interacts with the remote API to either create or update
    a project record based on its presence in the remote system.

    Arguments:
        project (object): The project object to be synchronized.

    Returns:
        int: The ID of the project in the remote system after synchronization.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    projects_url = f"{dj_api_url}/projects/"

    r = requests.get(projects_url, headers=headers)

    existing_projects = [p.get("openproject_id") for p in r.json()]
    openproject_id = project.get("openproject_id")
    if openproject_id in existing_projects:
        result = requests.patch(
            f"{projects_url}{openproject_id}/", json=project, headers=headers
        )
    else:
        result = requests.post(projects_url, json=project, headers=headers)

    return result.json()["id"]