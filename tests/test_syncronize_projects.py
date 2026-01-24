import unittest
from unittest.mock import patch, MagicMock

from windmill.u.admin.syncronize_projects import process_hook


class TestProcessHookFunction(unittest.TestCase):
    @patch("windmill.u.admin.syncronize_projects.requests.post")
    def test_creates_project_with_valid_data(self, mock_post):
        """
        Test process_hook creates a project with valid data.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "12345"}
        mock_post.return_value = mock_response

        action = "project:created"
        project = {"id": "001", "name": "Test Project"}
        projects_url = "https://api.example.com/projects/"
        headers = {"Authorization": "Bearer testtoken"}

        result = process_hook(action, project, projects_url, headers)

        mock_post.assert_called_once_with(
            projects_url, json=project, headers=headers
        )
        self.assertEqual("12345", result)

    @patch("windmill.u.admin.syncronize_projects.requests.patch")
    def test_updates_project_with_valid_data(self, mock_patch):
        """
        Test process_hook updates a project with valid data.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "001"}
        mock_patch.return_value = mock_response

        action = "project:updated"
        project = {"openproject_id": "001", "description": {"raw": "Updated description"}}
        projects_url = "https://api.example.com/projects/"
        headers = {"Authorization": "Bearer testtoken"}

        result = process_hook(action, project, projects_url, headers)

        mock_patch.assert_called_once_with(
            f'{projects_url}001/', json={"openproject_id": "001", "description": "Updated description"}, headers=headers
        )
        self.assertEqual("001", result)

    @patch("windmill.u.admin.syncronize_projects.requests.patch")
    def test_converts_dict_description_to_raw(self, mock_patch):
        """
        Test process_hook converts a dict description to raw string for an update.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "001"}
        mock_patch.return_value = mock_response

        action = "project:updated"
        project = {"id": "001", "description": {"raw": "Raw description"}}
        projects_url = "https://api.example.com/projects/"
        headers = {"Authorization": "Bearer testtoken"}

        result = process_hook(action, project, projects_url, headers)

        mock_patch.assert_called_once_with(
            f'{projects_url}001/', json={"id": "001", "openproject_id": "001", "description": "Raw description"}, headers=headers
        )
        self.assertEqual("001", result)

    @patch("windmill.u.admin.syncronize_projects.requests.post")
    def test_uses_default_description_if_missing_raw_key(self, mock_post):
        """
        Test process_hook sets default description if "raw" key is missing in the description dict.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "12345"}
        mock_post.return_value = mock_response

        action = "project:created"
        project = {"id": "002", "description": {}}
        projects_url = "https://api.example.com/projects/"
        headers = {"Authorization": "Bearer testtoken"}

        result = process_hook(action, project, projects_url, headers)

        mock_post.assert_called_once_with(
            projects_url, json={"id": "002", "openproject_id": "002", "description": ""}, headers=headers
        )
        self.assertEqual("12345", result)

    @patch("windmill.u.admin.syncronize_projects.requests.post")
    def test_infers_openproject_id_if_missing(self, mock_post):
        """
        Test process_hook infers openproject_id from the id key if it's missing.
        """
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "12346"}
        mock_post.return_value = mock_response

        action = "project:created"
        project = {"id": "003", "name": "Another Test Project"}
        projects_url = "https://api.example.com/projects/"
        headers = {"Authorization": "Bearer testtoken"}

        result = process_hook(action, project, projects_url, headers)

        mock_post.assert_called_once_with(
            projects_url, json={"id": "003", "openproject_id": "003", "name": "Another Test Project"}, headers=headers
        )
        self.assertEqual("12346", result)


if __name__ == "__main__":
    unittest.main()
