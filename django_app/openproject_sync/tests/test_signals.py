from openproject_sync import models
from openproject_sync import signals


class DummyResponse:
    def __init__(self, payload):
        self._payload = payload

    def json(self):
        return self._payload


def test_synchronize_project_to_openproject_create_posts_and_updates(monkeypatch, db):
    project = models.Project.objects.create(
        openproject_id=1,
        identifier="alpha",
        name="Alpha",
    )
    payload = {"id": 42}
    captured = {}

    def fake_post(url, json, headers):
        captured["url"] = url
        captured["json"] = json
        captured["headers"] = headers
        captured["json"]["id"] = 42
        return DummyResponse(payload)

    monkeypatch.setattr(signals.requests, "post", fake_post)
    monkeypatch.setattr(signals.settings, "OPENPROJECT_AUTHORIZATION_HASH", "auth")
    monkeypatch.setattr(signals.settings, "OPENPROJECT_API_URL", "https://example.test")

    result = signals.synchronize_project_to_openproject(
        models.Project,
        project,
        created=True,
    )

    project.refresh_from_db()
    assert payload == result
    assert 42 == project.openproject_id
    assert "https://example.test/api/v3/projects/" == captured["url"]
    assert project.to_openproject() == captured["json"]
    assert "Basic auth" == captured["headers"]["Authorization"]
    assert "application/json" == captured["headers"]["Content-Type"]


def test_synchronize_project_to_openproject_update_patches(monkeypatch, db):
    project = models.Project.objects.create(
        openproject_id=7,
        identifier="beta",
        name="Beta",
    )
    payload = {"id": 99}
    captured = {}

    def fake_patch(url, json, headers):
        captured["url"] = url
        captured["json"] = json
        captured["headers"] = headers
        captured["json"]["id"] = 99
        return DummyResponse(payload)

    monkeypatch.setattr(signals.requests, "patch", fake_patch)
    monkeypatch.setattr(signals.settings, "OPENPROJECT_AUTHORIZATION_HASH", "secret")
    monkeypatch.setattr(signals.settings, "OPENPROJECT_API_URL", "https://op.test")

    result = signals.synchronize_project_to_openproject(
        models.Project,
        project,
        created=False,
    )

    project.refresh_from_db()
    assert payload == result
    assert 99 == project.openproject_id
    assert "https://op.test/api/v3/projects/7/" == captured["url"]
    assert project.to_openproject() == captured["json"]
    assert "Basic secret" == captured["headers"]["Authorization"]
    assert "application/json" == captured["headers"]["Content-Type"]


def test_synchronize_project_to_openproject_returns_none_on_exception(monkeypatch, db):
    project = models.Project.objects.create(
        openproject_id=3,
        identifier="gamma",
        name="Gamma",
    )

    def fake_post(*_args, **_kwargs):
        raise RuntimeError("boom")

    monkeypatch.setattr(signals.requests, "post", fake_post)
    monkeypatch.setattr(signals.settings, "OPENPROJECT_AUTHORIZATION_HASH", "auth")
    monkeypatch.setattr(signals.settings, "OPENPROJECT_API_URL", "https://example.test")

    result = signals.synchronize_project_to_openproject(
        models.Project,
        project,
        created=True,
    )

    project.refresh_from_db()
    assert result is None
    assert 3 == project.openproject_id
