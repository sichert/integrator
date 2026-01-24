import requests
import wmill


def process_hook(action: str, time_entry: dict, url: str, headers: dict) -> str:
    """
    Processes a webhook action for a time entry and synchronizes data with an external service.

    This function is designed to handle webhook events by processing a given time entry
    dictionary and sending it to a specified URL. Depending on the action type, it makes
    either a PATCH or POST request to update or create records in the external system.
    Additionally, it ensures that the `openproject_id` field is appropriately assigned and
    the `description` field is normalized from a nested structure if needed.

    Arguments:
        action (str): The type of webhook action being performed (e.g., "time_entry:updated").
        time_entry (dict): A dictionary representing the time entry data to be synchronized.
        url (str): The endpoint URL of the external service where data needs to be sent.
        headers (dict): A dictionary containing HTTP request headers for authentication or
            other configurations.

    Returns:
        str: The ID of the processed time entry, as returned by the external service.

    Raises:
        Exception: If the HTTP request fails or if the response does not include the expected
            data structure.
    """
    if "openproject_id" not in time_entry and "id" in time_entry:
        time_entry["openproject_id"] = time_entry["id"]

    if "work_package" not in time_entry and "_embedded" in time_entry:
        work_package_id = wmill.run_script(
            "u/admin/get_work_package",
            args={"work_package_id": time_entry["_embedded"]["workPackage"]["id"]}
        )
        time_entry["work_package"] = work_package_id

    if "comment" in time_entry and type(time_entry["comment"]) is dict:
        time_entry["comment"] = time_entry["comment"].get("raw", "")

    if action == "time_entry:updated":
        print(f'{url}{time_entry["openproject_id"]}/')
        result = requests.patch(
            f'{url}{time_entry["openproject_id"]}/', json=time_entry, headers=headers
        )
    else:
        result = requests.post(url, json=time_entry, headers=headers)
    return result.json()["id"]


def main(
        action: str = "", time_entry: dict = {}, existing_time_entries: list = []
):
    """
    Main function for processing time entry actions and orchestrating payload handling.

    This function is a central entry point for processing time entry-related actions,
    either triggered by webhook payloads or through project requests. It determines the
    correct action to handle based on provided inputs and delegates processing to the
    `process_hook` function.

    Parameters:
    action : str
        The action type to process (e.g., "time_entry:created", "time_entry:updated").
    time_entry : dict
        The time entry data payload. Expected to include relevant keys such as
        "openproject_id" for determining action type.
    existing_time_entries : list
        A collection of existing time entries IDs, used to identify whether the
        `time_entry` corresponds to an update.

    Returns:
    tuple
        The result of processing the given action, as returned by `process_hook`.

    Raises:
    None
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    url = f"{dj_api_url}/time_entries/"

    if action and time_entry:
        # In case "action" is present in the input project, it means that we about to process a webhook payload.
        return process_hook(action, time_entry, url, headers)

    # Otherwise, we are dealing with a normal project request and do create the project payload ourself.
    action = "time_entry:created"
    openproject_id = time_entry.get("openproject_id", "")

    if openproject_id and openproject_id in existing_time_entries:
        action = "time_entry:updated"

    return process_hook(action, time_entry, url, headers)