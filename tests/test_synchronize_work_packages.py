import unittest
from unittest.mock import patch, MagicMock

from windmill.u.admin.synchronize_work_packages import process_hook


class TestProcessHook(unittest.TestCase):
    @patch('windmill.u.admin.synchronize_work_packages.requests.patch')
    def test_work_package_updated_action(self, mock_patch):
        """
        Test that process_hook sends a PATCH request when action is 'work_package:updated'.
        """
        work_package = {"id": "123", "description": {"raw": "Some description"}}
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "123"}
        mock_patch.return_value = mock_response

        result = process_hook(
            action="work_package:updated",
            work_package=work_package,
            work_packages_url="https://api.example.com/work_packages/",
            headers={"Authorization": "Bearer token"}
        )

        self.assertEqual("123", result)
        mock_patch.assert_called_once_with(
            "https://api.example.com/work_packages/123/",
            json={
                "id": "123",
                "openproject_id": "123",
                "description": "Some description",
            },
            headers={"Authorization": "Bearer token"}
        )

    @patch('windmill.u.admin.synchronize_work_packages.requests.post')
    def test_work_package_creation_action(self, mock_post):
        """
        Test that process_hook sends a POST request when action is not 'work_package:updated'.
        """
        work_package = {"id": "456", "description": {"raw": "Another description"}}
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "456"}
        mock_post.return_value = mock_response

        result = process_hook(
            action="work_package:created",
            work_package=work_package,
            work_packages_url="https://api.example.com/work_packages/",
            headers={"Authorization": "Bearer token"}
        )

        self.assertEqual("456", result)
        mock_post.assert_called_once_with(
            "https://api.example.com/work_packages/",
            json={
                "id": "456",
                "openproject_id": "456",
                "description": "Another description",
            },
            headers={"Authorization": "Bearer token"}
        )

    @patch('windmill.u.admin.synchronize_work_packages.requests.patch')
    def test_work_package_without_id_field(self, mock_patch):
        """
        Test that process_hook raises a KeyError exception when 'openproject_id' is missing.
        """
        work_package = {"description": {"raw": "Description without ID"}}
        mock_response = MagicMock()
        mock_response.json.return_value = {"id": "789"}
        mock_patch.return_value = mock_response
        with self.assertRaises(Exception) as context:
            process_hook(
                action="work_package:updated",
                work_package=work_package,
                work_packages_url="https://api.example.com/work_packages/",
                headers={"Authorization": "Bearer token"}
            )
        self.assertEqual(str(context.exception), "'openproject_id'")


if __name__ == "__main__":
    unittest.main()
