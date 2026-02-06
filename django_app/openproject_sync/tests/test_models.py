import pytest
from django.db import IntegrityError

from openproject_sync import models


def test_project_str_representation():
    project = models.Project(
        openproject_id=10,
        identifier="alpha",
        name="Alpha",
    )

    assert "alpha - Alpha" == str(project)


def test_project_to_openproject_returns_mapping():
    project = models.Project(
        openproject_id=25,
        identifier="beta",
        name="Beta",
        active=False,
        public=False,
        description="Client rollout",
    )

    assert {
        "id": 25,
        "identifier": "beta",
        "name": "Beta",
        "active": False,
        "public": False,
        "description": "Client rollout",
    } == project.to_openproject()


def test_project_to_openproject_includes_default_values():
    project = models.Project(
        openproject_id=31,
        identifier="gamma",
        name="Gamma",
    )

    assert {
        "id": 31,
        "identifier": "gamma",
        "name": "Gamma",
        "active": True,
        "public": True,
        "description": None,
    } == project.to_openproject()


def test_project_defaults_use_active_public_true():
    project = models.Project(
        openproject_id=30,
        identifier="gamma",
        name="Gamma",
    )

    assert True == project.active
    assert True == project.public
    assert None is project.description


@pytest.mark.django_db
def test_project_identifier_is_unique():
    models.Project.objects.create(
        openproject_id=40,
        identifier="unique-id",
        name="Unique One",
    )

    with pytest.raises(IntegrityError):
        models.Project.objects.create(
            openproject_id=41,
            identifier="unique-id",
            name="Unique Two",
        )
