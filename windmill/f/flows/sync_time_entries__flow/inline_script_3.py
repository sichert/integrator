# import wmill
from datetime import date, datetime
from typing import TypedDict


class TimeEntry(TypedDict):
    """
    Represents a dictionary-like data structure for time entry information.

    The TimeEntry class serves as a lightweight container for storing data
    related to a specific time entry. It includes fields for tracking
    identification, timing details, percentages related to task progress,
    costs, and other relevant details associated with the entry.

    Attributes:
        id: A unique identifier for the time entry.
        subject: The subject or title of the time entry.
        createdAt: The timestamp indicating when the time entry was created.
        updatedAt: The timestamp indicating when the time entry was last updated.
        derivedEstimatedTime: A string representation of the estimated time
            derived for the task.
        derivedRemainingTime: A string representation of the remaining time
            derived for the task.
        ignoreNonWorkingDays: A boolean indicating whether non-working days
            should be ignored in calculations.
        scheduleManually: A boolean indicating if the task is scheduled manually.
        percentageDone: A floating-point number representing the percentage of
            the task that has been completed.
        derivedPercentageDone: A floating-point number representing the derived
            percentage of completion for the task.
        date: The date associated with the time entry.
        spentTime: A string representation of the time spent on the task.
        estimatedTime: A string representing the total estimated time for the task.
        laborCosts: A string representation of the labor costs for the task.
        materialCosts: A string representation of the material costs for the task.
        overallCosts: A string representation of the overall costs for the task.
        description: A description or additional information about the time entry.
    """
    id: str
    subject: str
    createdAt: datetime
    updatedAt: datetime
    derivedEstimatedTime: str
    derivedRemainingTime: str
    ignoreNonWorkingDays: bool
    scheduleManually: bool
    percentageDone: float
    derivedPercentageDone: float
    date: date
    spentTime: str
    estimatedTime: str
    laborCosts: str
    materialCosts: str
    overallCosts: str
    description: str


def main(x: dict):
    """
    Parses a dictionary and returns a TimeEntry object by extracting values based on the provided keys.

    This function facilitates the creation of a TimeEntry object by mapping the keys from
    the input dictionary `x` to the corresponding attributes. Default values are applied
    if keys are missing or their values are not provided.

    Arguments:
        x (dict): A dictionary containing data to create a TimeEntry object.

    Returns:
        TimeEntry: An instance of the TimeEntry class populated with values extracted from `x`.
    """
    return TimeEntry(
        id=x["id"],
        subject=x["subject"],
        createdAt=x.get("createdAt",""),
        updatedAt=x.get("updatedAt",""),
        derivedEstimatedTime=x.get("derivedEstimatedTime",""),
        derivedRemainingTime=x.get("derivedRemainingTime",""),
        ignoreNonWorkingDays=x.get("ignoreNonWorkingDays", False),
        scheduleManually=x.get("scheduleManually", False),
        percentageDone=x.get("percentageDone", 0),
        derivedPercentageDone=x.get("derivedPercentageDone", 0),
        date=x.get("date",""),
        spentTime=x.get("spentTime",""),
        estimatedTime=x.get("estimatedTime",""),
        laborCosts=x.get("laborCosts",""),
        materialCosts=x.get("materialCosts",""),
        overallCosts=x.get("overallCosts",""),
        description=x.get("description", {"raw": ""}).get("raw",""),
    )