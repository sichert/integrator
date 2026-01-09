# import wmill


def main(x: dict):
    """
    Retrieves the "href" property of "workPackages" from the "_links" section of the input dictionary, if it exists.

    Parameters:
    x (dict): The input dictionary from which the desired value is extracted.

    Returns:
    str or None: The value of the "href" property under "workPackages" in the "_links" section, or None
    if any of the keys are missing.
    """
    return x.get("_links", {}).get("workPackages", {}).get("href")