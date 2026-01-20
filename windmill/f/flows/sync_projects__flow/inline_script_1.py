from typing import TypedDict


class Project(TypedDict):
    """
    Represents a structured format for storing project information.

    This class defines a TypedDict that holds information about a project, such as
    its identifier, name, status, and other attributes. It is used for type checking
    and ensuring consistency when handling project data.
    """
    openproject_id: int
    identifier: str
    name: str
    active: bool
    public: bool
    description: str


def main(x: dict):
    """
    Converts a dictionary input into a Project instance by mapping specific keys
    and providing default values for missing optional fields.

    Args:
        x (dict): A dictionary containing key-value pairs for the creation of
            a Project instance. Required keys include 'openproject_id',
            'identifier', and 'name'. Optional keys include 'active', 'public',
            and 'description' with a nested 'raw' key.

    Returns:
        Project: A new instance of the Project class initialized with values
            extracted from the input dictionary.
    """
    return Project(
        openproject_id=x["id"],
        identifier=x["identifier"],
        name=x["name"],
        active=x.get("active", True),
        public=x.get("public", True),
        description=x.get("description", {"raw": ""}).get("raw",""),
    )