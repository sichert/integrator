from django.db import models


class WorkPackage(models.Model):
    """
    Represents a work package, including details such as dates, costs, and descriptions.

    This class is a model used for managing work packages in a project management context.
    It includes fields to record and track important attributes such as time spent, estimated
    time, dates, and associated costs. Each work package also includes a description and summary.

    Attributes:
        openproject_id: The unique identifier of the work package in OpenProject.
        subject: A short title or summary for the work package.
        created_at: The timestamp when the work package was created.
        updated_at: The timestamp when the work package was last updated.
        derive_start_date: The start date derived from dependencies, optional.
        derive_due_date: The due date derived from dependencies, optional.
        start_date: The actual start date of the work package, optional.
        due_date: The planned due date of the work package, optional.
        spent_time: The amount of time spent on the work package, optional.
        estimated_time: The estimated amount of time required for the work package, optional.
        duration: The duration of the work package in terms of time, optional.
        labor_costs: Costs related to labor for the work package, optional.
        material_costs: Costs related to materials for the work package, optional.
        overall_costs: The total costs for the work package, optional.
        description: A detailed description of the work package, optional.
    """
    openproject_id = models.IntegerField()
    subject = models.CharField(max_length=255)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    derive_start_date = models.DateField(blank=True, null=True)
    derive_due_date = models.DateField(blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    spent_time = models.CharField(max_length=255, blank=True, null=True)
    estimated_time = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    labor_costs = models.CharField(max_length=255, blank=True, null=True)
    material_costs = models.CharField(max_length=255, blank=True, null=True)
    overall_costs = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)


class TimeEntry(models.Model):
    """
    Represents a time tracking entry associated with a specific project and work package.

    This class is used to model time tracking entries, including various attributes such as effort estimation,
    progress tracking, cost information, and time-related data. It facilitates the management of detailed project
    timelines and labor tracking.

    Attributes:
        openproject_id: The unique identifier of the time entry in OpenProject.
        project: An integer that represents the associated project identifier.
        work_package: A foreign key linking the time entry to a specific work package.
        subject: A string that provides the title or subject for this time entry.
        createdAt: The date and time when the time entry was created.
        updatedAt: The date and time when the time entry was last updated.
        derivedEstimatedTime: An optional string representing the calculated estimated time for the task.
        derivedRemainingTime: An optional string representing the calculated remaining time for the task.
        ignoreNonWorkingDays: A boolean indicating whether non-working days are excluded from scheduling calculations.
        scheduleManually: A boolean indicating whether scheduling is performed manually.
        percentageDone: A float indicating the percentage of work completed manually by the user.
        derivedPercentageDone: A float indicating the automatically calculated percentage of work completed.
        date: The date associated with this time entry.
        spentTime: An optional string indicating the amount of time already spent on the task.
        estimatedTime: An optional string indicating the estimated time required for the task.
        laborCosts: An optional string representing the labor costs associated with this task.
        materialCosts: An optional string representing the material costs associated with this task.
        overallCosts: An optional string representing the total costs for this task, including labor and materials.
        description: An optional text field containing additional details or comments about the time entry.
    """
    openproject_id = models.IntegerField()
    project = models.IntegerField()
    work_package = models.ForeignKey(WorkPackage, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    createdAt = models.DateTimeField(blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    derivedEstimatedTime = models.CharField(max_length=255, blank=True, null=True)
    derivedRemainingTime = models.CharField(max_length=255, blank=True, null=True)
    ignoreNonWorkingDays = models.BooleanField(default=False)
    scheduleManually = models.BooleanField(default=False)
    percentageDone = models.FloatField(default=0)
    derivedPercentageDone = models.FloatField(default=0)
    date = models.DateField(blank=True, null=True)
    spentTime = models.CharField(max_length=255, blank=True, null=True)
    estimatedTime = models.CharField(max_length=255, blank=True, null=True)
    laborCosts = models.CharField(max_length=255, blank=True, null=True)
    materialCosts = models.CharField(max_length=255, blank=True, null=True)
    overallCosts = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

