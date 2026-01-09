# import wmill
from datetime import date, datetime
from typing import TypedDict


class WorkPackage(TypedDict):
    """
    Represents a structured work package with detailed information.

    This TypedDict class is used to store and transfer structured data about a work package,
    including its metadata, timeline, time estimations, costs, and descriptions. It is intended
    to provide a comprehensive representation of a work package in various systems or APIs.

    Attributes:
        id: A unique identifier for the work package.
        subject: A brief descriptive title of the work package.
        createdAt: The date and time when the work package was created.
        updatedAt: The date and time when the work package was last updated.
        derivedStartDate: The calculated start date of the work package.
        derivedDueDate: The calculated due date of the work package.
        startDate: The manually specified or actual start date of the work package.
        dueDate: The manually specified or actual due date of the work package.
        spentTime: The total spent time on the work package in a descriptive format.
        estimatedTime: The estimated time required to complete the work package in a descriptive format.
        duration: The duration of the work package in a descriptive format.
        laborCosts: The total labor costs associated with the work package in a descriptive format.
        materialCosts: The total material costs associated with the work package in a descriptive format.
        overallCosts: The overall costs associated with the work package in a descriptive format.
        description: A detailed textual description or notes about the work package.
    """
    id: str
    subject: str
    createdAt: datetime
    updatedAt: datetime
    derivedStartDate: date
    derivedDueDate: date
    startDate: date
    dueDate: date
    spentTime: str
    estimatedTime: str
    duration: str
    laborCosts: str
    materialCosts: str
    overallCosts: str
    description: str


def main(x: dict):
    """
    Creates a new instance of a WorkPackage initialized with the provided dictionary.

    Parameters:
    x (dict): A dictionary containing the initialization data for the WorkPackage
        instance.

    Returns:
    WorkPackage: An instance of the WorkPackage class initialized with the
        provided data.
    """
    return WorkPackage(
        id=x["id"],
        subject=x["subject"],
        createdAt=x.get("createdAt", ""),
        updatedAt=x.get("updatedAt",""),
        derivedStartDate=x.get("derivedStartDate", ""),
        derivedDueDate=x.get("derivedDueDate", ""),
        startDate=x.get("startDate",""),
        dueDate=x.get("dueDate",""),
        spentTime=x.get("spentTime",""),
        estimatedTime=x.get("estimatedTime",""),
        duration=x.get("duration", ""),
        laborCosts=x.get("laborCosts",""),
        materialCosts=x.get("materialCosts",""),
        overallCosts=x.get("overallCosts",""),
        description=x.get("description", {"raw": ""}).get("raw",""),
    )