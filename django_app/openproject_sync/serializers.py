from rest_framework import serializers

from openproject_sync.models import TimeEntry, WorkPackage, Project


class SerializerWithSkipSignal(serializers.ModelSerializer):
    """
    Handles serialization tasks with a built-in mechanism to bypass specific model signals.

    This serializer extension ensures that specific signals related to
    the associated model are skipped during the creation and update
    operations. Primarily used for cases where signals need to be disabled
    for programmatic or performance reasons. Designed to work with Django
    Rest Framework serializers.

    Attributes:
        Meta.model: Specifies the model class associated with the
            serializer.
    """

    def create(self, validated_data):
        """
        Creates and saves a new instance of the model using the provided validated data.

        This method initializes a new instance of the model specified in the 'Meta.model'
        attribute using the validated data. The 'skip_signal' attribute is explicitly set
        to True to bypass specific signals during the save operation. After setting this
        property, the new model instance is saved to the database and returned.

        Parameters:
        validated_data (dict): A dictionary containing the validated data to initialize
                               the model instance.

        Returns:
        Model instance: The newly created model instance after saving it to the database.
        """
        ModelClass = self.Meta.model
        instance = ModelClass(
            **validated_data,
        )
        instance.skip_signal = True
        instance.save()
        return instance

    def update(self, instance, validated_data):
        """
        Updates an existing instance with the given validated data and sets a flag to skip signal processing.

        This method overrides the parent class's update method. Before updating the instance, it marks
        a specific flag to bypass any signal processing associated with the instance. The overridden
        method from the superclass is then called to perform the actual update operation.

        Parameters:
            instance: The object instance to be updated.
            validated_data: dict
                The validated data to update the instance with.

        Returns:
            The updated instance.
        """
        instance.skip_signal = True
        super().update(instance, validated_data)
        return instance

    class Meta:
        abstract = True


class ProjectSerializer(SerializerWithSkipSignal):
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
            "id",
            "openproject_id",
            "identifier",
            "name",
            "active",
            "public",
            "description",
        ]


class WorkPackageSerializer(SerializerWithSkipSignal):
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
            "lockVersion",
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


class TimeEntrySerializer(SerializerWithSkipSignal):
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
