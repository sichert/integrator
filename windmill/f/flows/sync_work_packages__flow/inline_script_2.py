# import wmill
from datetime import date, datetime
from typing import TypedDict


class WorkPackage(TypedDict):
    """
    A TypedDict representing a work package with various attributes related to scheduling,
    costs, time, and description.

    The WorkPackage class is used to model the data and characteristics of a specific
    work package within a project management or task scheduling system. It includes
    details such as identifiers, timestamps, scheduling information, and cost-related
    attributes which are essential for tracking and managing work progress.
    """
    openproject_id: int
    project: int
    subject: str
    createdAt: datetime
    updatedAt: datetime
    derivedStartDate: date
    derivedDueDate: date
    startDate: date
    dueDate: date
    spentTime: str
    estimatedTime: str
    derivedEstimatedTime: str
    derivedRemainingTime: str
    duration: str
    laborCosts: str
    materialCosts: str
    overallCosts: str
    description: str
    scheduleManually: bool
    ignoreNonWorkingDays: bool
    percentageDone: int
    derivedPercentageDone: int


def main(x: dict, project_id: int):
    """
    Converts a dictionary representation of a work package into a WorkPackage object.

    This function maps the keys of the input dictionary to the corresponding attributes
    of the WorkPackage object. If certain keys are not present in the dictionary, default
    values are assigned. It ensures that the WorkPackage object is correctly populated
    with relevant information.

    Arguments:
        x (dict): A dictionary containing information to create a WorkPackage object.
                  The dictionary must include an "id" key for the work package ID and
                  a "subject" key for the work package subject. Other keys in the dictionary
                  are optional but used if present.

    Returns:
        WorkPackage: An object with attributes populated based on the input dictionary.
    """
    return WorkPackage(
        openproject_id=x["id"],
        project=project_id,
        subject=x["subject"],
        createdAt=x.get("createdAt", ""),
        updatedAt=x.get("updatedAt",""),
        derivedStartDate=x.get("derivedStartDate", ""),
        derivedDueDate=x.get("derivedDueDate", ""),
        startDate=x.get("startDate",""),
        dueDate=x.get("dueDate",""),
        spentTime=x.get("spentTime",""),
        estimatedTime=x.get("estimatedTime",""),
        derivedEstimatedTime=x.get("derivedEstimatedTime",""),
        derivedRemainingTime=x.get("derivedRemainingTime",""),
        duration=x.get("duration", ""),
        laborCosts=x.get("laborCosts",""),
        materialCosts=x.get("materialCosts",""),
        overallCosts=x.get("overallCosts",""),
        description=x.get("description", {"raw": ""}).get("raw",""),
        scheduleManually=x.get("scheduleManually", False),
        ignoreNonWorkingDays=x.get("ignoreNonWorkingDays", False),
        percentageDone=x.get("percentageDone", 0),
        derivedPercentageDone=x.get("derivedPercentageDone", 0),
    )