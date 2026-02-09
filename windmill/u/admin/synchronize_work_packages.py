import requests
import wmill


def process_hook(
    action: str, work_package: dict, work_packages_url: str, headers: dict
) -> str:
    """
    Processes a webhook action for updating or creating work packages.

    The function processes a webhook action by updating the work package if it
    already exists or creating a new one if it doesn't. It ensures that necessary
    fields are present or formatted appropriately in the provided work package
    before sending an HTTP request.

    Parameters:
    action : str
        The action type indicating whether a work package is being updated or created.
    work_package : dict
        The work package data that needs to be processed.
    work_packages_url : str
        The base URL for the work packages API endpoint.
    headers : dict
        The HTTP headers required for the API request.

    Returns:
    str
        The ID of the processed work package as returned by the API.
    """
    if "openproject_id" not in work_package and "id" in work_package:
        work_package["openproject_id"] = work_package["id"]

    if "_embedded" in work_package:
        project_id = wmill.run_script(
            "u/admin/get_project",
            args={"project_id": work_package["_embedded"]["project"]["id"]},
        )
        work_package["project"] = project_id

    if "description" in work_package and type(work_package["description"]) is dict:
        work_package["description"] = work_package["description"].get("raw", "")

    if action == "work_package:updated":
        result = requests.patch(
            f"{work_packages_url}{work_package['openproject_id']}/",
            json=work_package,
            headers=headers,
        )
    else:
        result = requests.post(work_packages_url, json=work_package, headers=headers)
    return result.json()["id"]


def main(action: str = "", work_package: dict = {}, existing_work_packages: list = []):
    """
    Main function for handling work package operations.

    This function is responsible for processing webhook payloads or creating project
    payloads based on the provided input. It interacts with external services to
    retrieve necessary variables, constructs appropriate HTTP headers, and
    delegates further processing to the `process_hook` function.

    Parameters:
    action: str
        Defines the action to perform. It could be a webhook action or an action
        for normal project execution. Defaults to an empty string.
    work_package: dict
        A dictionary containing details of the work package to process. Defaults
        to an empty dictionary.
    existing_work_packages: list
        A list of work packages that already exist, used for determining whether
        the action is a creation or an update. Defaults to an empty list.

    Returns:
    Any
        The result of the `process_hook` function, which handles the defined
        action on the specified work package.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    work_packages_url = f"{dj_api_url}/work_packages/"

    if action and work_package:
        # In case "action" is present in the input project, it means that we about to process a webhook payload.
        return process_hook(action, work_package, work_packages_url, headers)

    # Otherwise, we are dealing with a normal project request and do create the project payload ourself.
    action = "work_package:created"
    openproject_id = work_package.get("openproject_id", "")

    if openproject_id and openproject_id in existing_work_packages:
        action = "work_package:updated"

    return process_hook(action, work_package, work_packages_url, headers)
