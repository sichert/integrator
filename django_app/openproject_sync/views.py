from rest_framework import permissions, viewsets

from openproject_sync.models import Project, WorkPackage, TimeEntry
from openproject_sync.serializers import ProjectSerializer, TimeEntrySerializer, WorkPackageSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Handles operations related to Project objects.

    This class provides a view set for performing CRUD operations on Project
    objects. It utilizes a model serializer for handling data representation
    and applies required authentication permissions.

    Attributes:
        queryset: A QuerySet containing all the Project objects.
        serializer_class: The serializer class used for Project data.
        permission_classes: A list of permission classes applied to all the
            view set actions.
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'openproject_id'
    permission_classes = [permissions.IsAuthenticated]


class WorkPackageViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing work packages.

    The WorkPackageViewSet provides an interface for creating, retrieving, updating,
    and deleting work packages. This viewset utilizes Django REST Framework's
    ModelViewSet to automatically handle common behaviors for a set of model-based
    views.

    The viewset restricts access to authenticated users only.

    Attributes:
        queryset (QuerySet): The set of WorkPackage objects to operate upon.
        serializer_class (type): The serializer class used to convert querysets
            into JSON and validate input data.
        permission_classes (list): The list of permission classes applied to
            the viewset to enforce access control.
    """
    queryset = WorkPackage.objects.all()
    serializer_class = WorkPackageSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'openproject_id'


class TimeEntryViewSet(viewsets.ModelViewSet):
    """
    A viewset for managing TimeEntry instances.

    This class provides a ModelViewSet implementation for handling HTTP requests
    related to TimeEntry objects. It provides actions for creating, retrieving,
    updating, and deleting TimeEntry records. The viewset ensures that only
    authenticated users can access its endpoints.

    Attributes:
        queryset: A queryset containing all TimeEntry objects.
        serializer_class: The serializer class used for TimeEntry objects.
        permission_classes: A list of permission classes applied to this viewset.
    """
    queryset = TimeEntry.objects.all()
    serializer_class = TimeEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'openproject_id'