# import wmill
from datetime import date, datetime
from typing import TypedDict


class TimeEntry(TypedDict):
    """
    Structured data representation of a time entry.

    This class is a typed dictionary that defines the structure of a time entry. It is used
    to provide a strongly-typed way to represent and work with time entry data, ensuring the
    consistency of its format. Each field corresponds to relevant details associated with a
    time-tracking entry.

    Attributes:
        openproject_id: An integer representing the ID of the time entry in the OpenProject system.
        work_package: An integer indicating the associated work package for the time entry.
        ongoing: A boolean indicating whether the time entry is currently ongoing.
        comment: A string containing any comments or notes related to the time entry.
        spentOn: A date representing the day the time was spent.
        hours: A string specifying the amount of time spent, typically in a formatted manner.
        createdAt: A datetime object indicating when this time entry was created.
        updatedAt: A datetime object representing the last time this time entry was updated.
    """
    openproject_id: int
    work_package: int
    ongoing: bool
    comment: str
    spentOn: date
    hours: str
    createdAt: datetime
    updatedAt: datetime


def main(x: dict, work_package_id: int):
    """
    Transforms input dictionary and work package ID into a TimeEntry object.

    This function extracts relevant data from the input dictionary and combines it
    with the given work package ID to create and return a TimeEntry object. It
    handles optional values within the input dictionary by providing default values
    where necessary.

    Parameters:
    x : dict
        Dictionary containing the source data to create the TimeEntry object.
        Expected keys include "id", "ongoing" (optional), "comment" (optional),
        "comment.raw" (optional), "spentOn" (optional), "hours" (optional),
        "createdAt" (optional), and "updatedAt" (optional).
    work_package_id : int
        Identifier for the associated work package.

    Returns:
    TimeEntry
        An instance of TimeEntry initialized with the provided data.
    """
    return TimeEntry(
        openproject_id=x["id"],
        work_package=work_package_id,
        ongoing=x.get("ongoing", False),
        comment=x.get("comment", {}).get("raw", ""),
        spentOn=x.get("spentOn", ""),
        hours=x.get("hours", ""),
        createdAt=x.get("createdAt", ""),
        updatedAt=x.get("updatedAt", ""),
    )
