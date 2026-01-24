import requests
import wmill


def main():
    """
    Fetches time entry data via an API call and extracts OpenProject IDs.

    This function retrieves the API authorization credentials and URL from predefined variables.
    It sends a GET request to the endpoint for retrieving time entry data. The API response is
    expected to be in JSON format, and the function extracts the 'openproject_id' values from
    the time entry objects contained within the response.

    Returns:
        List[int | None]: A list containing the 'openproject_id' extracted from the time
        entries returned by the API. If a time entry object lacks the 'openproject_id' key,
        None will be included in the list.

    Raises:
        Any exceptions raised during the network request or JSON decoding will propagate
        to the caller.
    """
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    r = requests.get(f"{dj_api_url}/time_entries/", headers=headers)
    return [p.get("openproject_id") for p in r.json()]