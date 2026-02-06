from django.db import models


class OpenProjectModelMixin(models.Model):
    """
    A mixin class for integrating OpenProject IDs into models.

    This mixin provides the functionality to associate a model with an
    OpenProject ID. It is designed to be used as an abstract base class,
    allowing other models to inherit from it and include the `openproject_id`
    field for managing integration with the OpenProject platform.
    """

    openproject_id = models.IntegerField()

    class Meta:
        abstract = True


class Project(OpenProjectModelMixin, models.Model):
    """
    Represents a project entity within the system.

    This class is used to define the structure and behavior of a project in the application.
    Projects are uniquely identified by their identifier, have a name, and can have additional
    attributes such as being active, public, and a textual description.

    Fields:
        identifier (str): A unique identifier for the project.
        name (str): The name of the project.
        active (bool): Indicates whether the project is active. Defaults to True.
        public (bool): Indicates whether the project is public. Defaults to True.
        description (str or None): An optional textual description of the project.

    Meta:
        ordering (tuple[str]): The default ordering for querysets is by the project name.
        verbose_name_plural (str): The plural name for the class in the admin interface is 'Projects'.

    Returns:
        str: A string representation of the project, consisting of its identifier and name.
    """

    identifier = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    active = models.BooleanField(default=True)
    public = models.BooleanField(default=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.identifier} - {self.name}"

    def to_openproject(self):
        """
        Converts the instance attributes into a dictionary format compatible with OpenProject.

        Returns
        -------
        dict
            A dictionary containing the mapped attributes: `identifier`, `name`, `active`,
            `public`, and `description` (formatted as a nested dictionary with a key `raw`).
        """
        return {
            "_type": "Project",
            "id": self.openproject_id,
            "identifier": self.identifier,
            "name": self.name,
            "active": str(self.active),
            "public": str(self.public),
            "description": {"raw": self.description},
        }


class WorkPackage(OpenProjectModelMixin, models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    createdAt = models.DateTimeField(blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    derivedStartDate = models.DateTimeField(blank=True, null=True)
    derivedDueDate = models.DateTimeField(blank=True, null=True)
    startDate = models.DateField(blank=True, null=True)
    dueDate = models.DateField(blank=True, null=True)
    spentTime = models.CharField(max_length=255, blank=True, null=True)
    estimatedTime = models.CharField(max_length=255, blank=True, null=True)
    derivedEstimatedTime = models.CharField(max_length=255, blank=True, null=True)
    derivedRemainingTime = models.CharField(max_length=255, blank=True, null=True)
    duration = models.CharField(max_length=255, blank=True, null=True)
    laborCosts = models.CharField(max_length=255, blank=True, null=True)
    materialCosts = models.CharField(max_length=255, blank=True, null=True)
    overallCosts = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    scheduleManually = models.BooleanField(default=False)
    ignoreNonWorkingDays = models.BooleanField(default=False)
    percentageDone = models.IntegerField(blank=True, null=True)
    derivedPercentageDone = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = ("subject",)
        verbose_name_plural = "Work Packages"

    def __str__(self):
        return f"{self.project} - {self.subject}"


class TimeEntry(OpenProjectModelMixin, models.Model):
    work_package = models.ForeignKey(WorkPackage, on_delete=models.CASCADE)
    ongoing = models.BooleanField(default=False)
    comment = models.TextField(blank=True, null=True)
    spentOn = models.DateField(blank=True, null=True)
    hours = models.CharField(max_length=255, blank=True, null=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("work_package", "spentOn")
        verbose_name_plural = "Time Entries"

    def __str__(self):
        return f"{self.work_package} - {self.spentOn} - {self.hours}"
