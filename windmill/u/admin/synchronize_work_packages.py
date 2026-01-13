import requests
import wmill


def main(work_package: object):
    """
    Handles the creation or update of a work package on a remote service via API interaction.

    The function determines if a work package with a given `openproject_id` already exists on the
    remote service. If it exists, the work package is updated. If it does not exist, a new work
    package is created. The function communicates with the API using HTTP requests.

    Parameters:
    work_package: object
        The work package data to be sent to the remote service. The object should include
        an `openproject_id` field which identifies the work package.

    Returns:
    int
        The ID of the created or updated work package as returned by the remote service.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    work_packages_url = f"{dj_api_url}/work_packages/"

    r = requests.get(work_packages_url, headers=headers)

    existing_projects = [p.get("openproject_id") for p in r.json()]
    openproject_id = work_package.get("openproject_id")
    if openproject_id in existing_projects:
        result = requests.patch(
            f"{work_packages_url}{openproject_id}/", json=work_package, headers=headers
        )
    else:
        result = requests.post(work_packages_url, json=work_package, headers=headers)

    return result.json().get("id")
