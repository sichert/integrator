from rest_framework import serializers

from openproject_sync.models import TimeEntry, WorkPackage, Project


class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Project model.

    This serializer is used to map the Project model data to and from various
    representations such as JSON. It provides controlled access to specific
    fields and ensures proper serialization and deserialization of Project
    instances, making it suitable for API interactions.

    Attributes:
        model (type): Specifies the model to be serialized.
        fields (list): Defines the fields included in the serialized output.
    """
    class Meta:
        model = Project
        fields = [
            "id", "openproject_id", "identifier", "name", "active", "public", "description"
        ]


class WorkPackageSerializer(serializers.ModelSerializer):
    """
    Serializer class for the WorkPackage model.

    The serializer converts model instances into representations such as JSON and
    validates data passed to it for creating or updating WorkPackage instances. It is
    used as part of Django's REST framework to handle API interactions related to the
    WorkPackage model.

    Attributes:
        model (type): Specifies the model to be serialized.
        fields (list): Defines the fields included in the serialized output.
    """

    class Meta:
        model = WorkPackage
        fields = [
            "id",
            "openproject_id",
            "subject",
            "project",
            "subject",
            "createdAt",
            "updatedAt",
            "derivedStartDate",
            "derivedDueDate",
            "startDate",
            "dueDate",
            "spentTime",
            "estimatedTime",
            "derivedEstimatedTime",
            "derivedRemainingTime",
            "duration",
            "laborCosts",
            "materialCosts",
            "overallCosts",
            "description",
            "scheduleManually",
            "ignoreNonWorkingDays",
            "percentageDone",
            "derivedPercentageDone",
        ]


class TimeEntrySerializer(serializers.ModelSerializer):
    """
    Serializer class for TimeEntry model.

    This class is responsible for serializing and deserializing TimeEntry model data.
    It defines the fields that should be included while transforming the model
    data into a serialized format or processing serialized data for model creation
    or updates.

    Attributes:
        model (type): Specifies the model to be serialized.
        fields (list): Defines the fields included in the serialized output.
    """

    class Meta:
        model = TimeEntry
        fields = [
            "id",
            "openproject_id",
            "work_package",
            "ongoing",
            "comment",
            "spentOn",
            "hours",
            "createdAt",
            "updatedAt",
        ]
