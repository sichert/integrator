import requests
import wmill


def process_hook(action: str, project: dict, projects_url: str, headers: dict) -> str:
    """
    Processes a webhook action related to a project and interacts with an external service to
    update or create the project accordingly.

    Parameters:
    action : str
        The type of action being performed on the project (e.g., "project:updated").
    project : dict
        A dictionary containing the project details. The dictionary may include keys like
        "id" or "description".
    projects_url : str
        The URL endpoint for interacting with the projects resource of the external service.
    headers : dict
        The HTTP headers to include with the request to the external service.

    Returns:
    str
        The ID of the project as returned by the external service.
    """
    if "openproject_id" not in project and "id" in project:
        project["openproject_id"] = project["id"]

    if "description" in project and type(project["description"]) is dict:
        project["description"] = project["description"].get("raw", "")

    if action == "project:updated":
        result = requests.patch(
            f'{projects_url}{project["openproject_id"]}/', json=project, headers=headers
        )
    else:
        result = requests.post(projects_url, json=project, headers=headers)
    return result.json()["id"]


def main(action: str = "", project: dict = {}, existing_projects: list = []):
    """
    Processes project actions with webhook payload and determines whether to create or update a project
    based on the provided parameters and existing project criteria.

    Parameters:
    action (str): Specifies the type of action. Default is an empty string.
    project (dict): The project data to process. Default is an empty dictionary.
    existing_projects (list): A list of existing project identifiers.

    Returns:
    Any: The result of the process_hook function, applicable to the performed action.

    Raises:
    None
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    projects_url = f"{dj_api_url}/projects/"

    if action and project:
        # In case "action" is present in the input project, it means that we about to process a webhook payload.
        return process_hook(action, project, projects_url, headers)

    # Otherwise, we are dealing with a normal project request and do create the project payload ourself.
    action = "project:created"
    openproject_id = project.get("openproject_id", "")

    if openproject_id and openproject_id in existing_projects:
        action = "project:updated"

    return process_hook(action, project, projects_url, headers)
