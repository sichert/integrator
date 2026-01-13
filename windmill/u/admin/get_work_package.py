import requests
import wmill


def main(work_package_id: int):
    authorization_hash = wmill.get_variable("u/admin/dj_authorization_hash")
    dj_api_url = wmill.get_variable("u/admin/dj_api_url")
    headers = {"Authorization": f"Basic {authorization_hash}"}
    work_packages_url = f"{dj_api_url}/work_packages/{work_package_id}"

    r = requests.get(work_packages_url, headers=headers)

    return r.json().get("id")