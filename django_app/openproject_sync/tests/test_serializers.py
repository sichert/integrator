import datetime

import pytest
from django.utils import timezone

from openproject_sync import models
from openproject_sync import serializers


@pytest.mark.django_db
def test_work_package_serializer_outputs_expected_fields():
    """
    Assert serializer output includes the expected field set.
    """
    project = models.Project.objects.create(
        openproject_id=101,
        identifier="proj-1",
        name="Project One",
        active=True,
        public=True,
    )
    work_package = models.WorkPackage.objects.create(
        openproject_id=202,
        project=project,
        subject="Initial setup",
        createdAt=timezone.now(),
        updatedAt=timezone.now(),
        startDate=datetime.date(2024, 1, 2),
        dueDate=datetime.date(2024, 1, 5),
        scheduleManually=True,
        ignoreNonWorkingDays=False,
        percentageDone=30,
        derivedPercentageDone=40,
    )

    data = serializers.WorkPackageSerializer(work_package).data

    expected_keys = {
        "id",
        "openproject_id",
        "subject",
        "project",
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
    }

    assert expected_keys == set(data.keys())
    assert work_package.openproject_id == data["openproject_id"]
    assert work_package.project_id == data["project"]
    assert work_package.subject == data["subject"]
    assert work_package.scheduleManually == data["scheduleManually"]
    assert work_package.ignoreNonWorkingDays == data["ignoreNonWorkingDays"]


@pytest.mark.django_db
def test_work_package_serializer_creates_instance():
    """
    Assert serializer creates a WorkPackage with provided fields.
    """
    project = models.Project.objects.create(
        openproject_id=303,
        identifier="proj-2",
        name="Project Two",
        active=True,
        public=True,
    )
    payload = {
        "openproject_id": 404,
        "project": project.id,
        "subject": "API integration",
        "scheduleManually": False,
        "ignoreNonWorkingDays": True,
    }

    serializer = serializers.WorkPackageSerializer(data=payload)

    assert serializer.is_valid(), serializer.errors

    work_package = serializer.save()

    assert payload["openproject_id"] == work_package.openproject_id
    assert payload["project"] == work_package.project_id
    assert payload["subject"] == work_package.subject
    assert payload["scheduleManually"] == work_package.scheduleManually
    assert payload["ignoreNonWorkingDays"] == work_package.ignoreNonWorkingDays


@pytest.mark.django_db
def test_work_package_serializer_requires_project():
    """
    Assert serializer requires project field.
    """
    payload = {
        "openproject_id": 505,
        "subject": "Missing project",
    }

    serializer = serializers.WorkPackageSerializer(data=payload)

    assert not serializer.is_valid()
    assert {"project"} == set(serializer.errors.keys())


@pytest.mark.django_db
def test_work_package_serializer_requires_subject():
    """
    Assert serializer requires subject field.
    """
    project = models.Project.objects.create(
        openproject_id=606,
        identifier="proj-3",
        name="Project Three",
        active=True,
        public=True,
    )
    payload = {
        "openproject_id": 707,
        "project": project.id,
    }

    serializer = serializers.WorkPackageSerializer(data=payload)

    assert not serializer.is_valid()
    assert {"subject"} == set(serializer.errors.keys())


@pytest.mark.django_db
def test_work_package_serializer_defaults_boolean_flags():
    """
    Assert serializer applies default boolean values when omitted.
    """
    project = models.Project.objects.create(
        openproject_id=606,
        identifier="proj-3",
        name="Project Three",
        active=True,
        public=True,
    )
    payload = {
        "openproject_id": 707,
        "project": project.id,
        "subject": "Defaults check",
    }

    serializer = serializers.WorkPackageSerializer(data=payload)

    assert serializer.is_valid(), serializer.errors

    work_package = serializer.save()

    assert False is work_package.scheduleManually
    assert False is work_package.ignoreNonWorkingDays


@pytest.mark.django_db
def test_project_serializer_outputs_expected_fields():
    """
    Assert serializer output includes the expected field set.
    """
    project = models.Project.objects.create(
        openproject_id=808,
        identifier="proj-4",
        name="Project Four",
        active=False,
        public=True,
        description="Initial rollout",
    )

    data = serializers.ProjectSerializer(project).data

    expected_keys = {
        "id",
        "openproject_id",
        "identifier",
        "name",
        "active",
        "public",
        "description",
    }

    assert expected_keys == set(data.keys())
    assert project.openproject_id == data["openproject_id"]
    assert project.identifier == data["identifier"]
    assert project.name == data["name"]
    assert project.active == data["active"]
    assert project.public == data["public"]
    assert project.description == data["description"]


@pytest.mark.django_db
def test_project_serializer_creates_instance_with_defaults():
    """
    Assert serializer creates a Project and applies model defaults.
    """
    payload = {
        "openproject_id": 909,
        "identifier": "proj-5",
        "name": "Project Five",
    }

    serializer = serializers.ProjectSerializer(data=payload)

    assert serializer.is_valid(), serializer.errors

    project = serializer.save()

    assert payload["openproject_id"] == project.openproject_id
    assert payload["identifier"] == project.identifier
    assert payload["name"] == project.name
    assert True is project.active
    assert True is project.public
    assert project.description is None


@pytest.mark.django_db
def test_project_serializer_requires_identifier():
    """
    Assert serializer requires identifier field.
    """
    payload = {
        "openproject_id": 1001,
        "name": "Missing identifier",
    }

    serializer = serializers.ProjectSerializer(data=payload)

    assert not serializer.is_valid()
    assert {"identifier"} == set(serializer.errors.keys())


@pytest.mark.django_db
def test_project_serializer_requires_name():
    """
    Assert serializer requires name field.
    """
    payload = {
        "openproject_id": 1002,
        "identifier": "proj-6",
    }

    serializer = serializers.ProjectSerializer(data=payload)

    assert not serializer.is_valid()
    assert {"name"} == set(serializer.errors.keys())


@pytest.mark.django_db
def test_project_serializer_updates_instance():
    """
    Assert serializer updates an existing Project instance.
    """
    project = models.Project.objects.create(
        openproject_id=1003,
        identifier="proj-7",
        name="Project Seven",
        active=True,
        public=True,
    )
    payload = {
        "openproject_id": project.openproject_id,
        "identifier": project.identifier,
        "name": "Project Seven Updated",
        "active": False,
        "public": False,
        "description": "Updated description",
    }

    serializer = serializers.ProjectSerializer(project, data=payload)

    assert serializer.is_valid(), serializer.errors

    updated_project = serializer.save()

    assert payload["name"] == updated_project.name
    assert payload["active"] == updated_project.active
    assert payload["public"] == updated_project.public
    assert payload["description"] == updated_project.description
