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

    def create(self, validated_data):
        """
        Creates and saves a new Project instance.

        This method is used to create a new instance of the Project model using
        the provided validated data. It ensures that the "skip_signal" attribute
        is set to True prior to saving the object. The saved Project instance
        is then returned.

        Args:
            validated_data (dict): A dictionary containing validated data needed
            to create the Project instance.

        Returns:
            Project: The newly created and saved Project instance.
        """
        project = Project(
            **validated_data,
        )
        project.skip_signal = True
        project.save()
        return project

    def update(self, instance, validated_data):
        """
        Updates an existing instance with the provided validated data.

        This method overrides the default update behavior to set a flag
        on the instance, which can be used to skip specific signals or
        perform conditional logic during the update process. After setting
        the flag, the method delegates the update to the parent implementation.

        Args:
            instance: The instance to be updated.
            validated_data: The validated data used to update the instance.

        Returns:
            The updated instance.
        """
        instance.skip_signal = True
        super().update(instance, validated_data)
        return instance

    class Meta:
        model = Project
        fields = [
            "id",
            "openproject_id",
            "identifier",
            "name",
            "active",
            "public",
            "description",
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
