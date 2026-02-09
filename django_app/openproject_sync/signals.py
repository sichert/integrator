from functools import wraps

import requests
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_app import settings
from .models import Project, WorkPackage, TimeEntry


def skip_signal():
    """
    Decorator to skip signal handling under specific conditions.

    This decorator is used to limit the execution of a signal handling function
    based on the presence of a `skip_signal` attribute in the instance being processed.
    If the attribute is present, the signal handling is skipped.

    Raises
    ------
    None
    """

    def _skip_signal(signal_func):
        @wraps(signal_func)
        def _decorator(sender, instance, **kwargs):
            if hasattr(instance, "skip_signal"):
                return None
            return signal_func(sender, instance, **kwargs)

        return _decorator

    return _skip_signal


@receiver(post_save, sender=Project)
@skip_signal()
def synchronize_project_to_openproject(sender, instance, created, **kwargs):
    """
    Signal to synchronize a Project instance with the OpenProject system on creation
    or update.

    This function listens to the `post_save` signal for the `Project` model and sends
    the model's data to the OpenProject API when a new instance is created or an existing
    one is updated. The synchronization operation utilizes the API authorization details
    and base URL defined in the application settings.

    Args:
        sender: The model class that sent the signal.
        instance: The instance of the sender being saved.
        created: A boolean indicating whether the instance was created (True) or updated (False).
        **kwargs: Additional keyword arguments passed by the signal.

    Returns:
        The JSON response from the OpenProject API after a successful synchronization.
    """
    authorization_hash = settings.OPENPROJECT_AUTHORIZATION_HASH
    op_api_url = settings.OPENPROJECT_API_URL
    try:
        data = instance.to_openproject()
        if created:
            r = requests.post(
                f"{op_api_url}/api/v3/projects/",
                json=data,
                headers={
                    "Authorization": f"Basic {authorization_hash}",
                    "Content-Type": "application/json",
                },
            )
        else:
            r = requests.patch(
                f"{op_api_url}/api/v3/projects/{instance.openproject_id}/",
                json=data,
                headers={
                    "Authorization": f"Basic {authorization_hash}",
                    "Content-Type": "application/json",
                },
            )
        response = r.json()
        Project.objects.filter(id=instance.id).update(openproject_id=response["id"])
        return response
    except Exception as e:
        pass
