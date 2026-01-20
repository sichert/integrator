import unittest
from unittest.mock import patch, MagicMock

import requests

from windmill.f.flows.sync_work_packages__flow.inline_script_0 import main


class TestMainFunction(unittest.TestCase):

    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.wmill.get_variable')
    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.requests.get')
    def test_returns_empty_list_on_empty_response(self, mock_get, mock_get_variable):
        """
        Tests the behavior of main function when API response is empty.

        This test case ensures that when the external API returns an empty response,
        the main function correctly processes the data and returns an empty list.
        It uses mocking to simulate external dependencies and their behavior.

        Arguments:
            self: Refers to the instance of the test class.

        Attributes:
            mock_get: Mock of the `requests.get` function to simulate API calls.
            mock_get_variable: Mock of the `get_variable` function to provide
                predetermined variable values.

        Raises:
            AssertionError: If the returned result is not an empty list.
        """
        mock_get_variable.side_effect = lambda key: "mock_value"
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response

        result = main()
        self.assertEqual([], result)

    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.wmill.get_variable')
    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.requests.get')
    def test_raises_exception_on_failed_request(self, mock_get, mock_get_variable):
        """
        Test that the main function raises a requests.RequestException
        if the request to the API fails.
        """
        mock_get_variable.side_effect = lambda key: "mock_value"
        mock_get.side_effect = requests.RequestException

        with self.assertRaises(requests.RequestException):
            main()

    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.wmill.get_variable')
    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.requests.get')
    def test_returns_list_of_projects(self, mock_get, mock_get_variable):
        """
        Test that the main function returns a list of projects
        when the API response contains valid project data.
        """
        mock_get_variable.side_effect = lambda key: "mock_value"
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "_embedded": {"elements": [{"id": 1, "name": "Project A"}, {"id": 2, "name": "Project B"}]}
        }
        mock_get.return_value = mock_response

        result = main()
        expected = [{"id": 1, "name": "Project A"}, {"id": 2, "name": "Project B"}]
        self.assertEqual(expected, result)

    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.wmill.get_variable')
    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_0.requests.get')
    def test_returns_empty_list_when_no_embedded_elements(self, mock_get, mock_get_variable):
        """
        Test that the main function handles cases where "_embedded"
        and "elements" keys are missing or empty in the API response,
        returning an empty list.
        """
        mock_get_variable.side_effect = lambda key: "mock_value"
        mock_response = MagicMock()
        mock_response.json.return_value = {"_embedded": {}}
        mock_get.return_value = mock_response

        result = main()
        self.assertEqual([], result)
