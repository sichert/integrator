import unittest
from unittest.mock import patch, MagicMock

import requests

from windmill.f.flows.sync_work_packages__flow.inline_script_2 import main


class TestMainFunction(unittest.TestCase):

    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_2.wmill.get_variable')
    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_2.requests.get')
    def test_returns_empty_list_when_no_embedded_elements(self, mock_get, mock_get_variable):
        """
        Test that the main function returns an empty list
        if the API response does not contain any elements.
        """
        mock_get_variable.side_effect = lambda key: "mock_value"
        mock_response = MagicMock()
        mock_response.json.return_value = {}
        mock_get.return_value = mock_response
        result = main("/endpoint")
        self.assertEqual([], result)

    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_2.wmill.get_variable')
    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_2.requests.get')
    def test_returns_list_of_elements(self, mock_get, mock_get_variable):
        """
        Test that the main function returns a list of elements
        when they are present in the API response.
        """
        mock_get_variable.side_effect = lambda key: "mock_value"
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "_embedded": {
                "elements": [{"id": 1, "name": "Element1"}, {"id": 2, "name": "Element2"}]
            }
        }
        mock_get.return_value = mock_response
        result = main("/endpoint")
        self.assertEqual(
            [{"id": 1, "name": "Element1"}, {"id": 2, "name": "Element2"}],
            result
        )

    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_2.wmill.get_variable')
    @patch('windmill.f.flows.sync_work_packages__flow.inline_script_2.requests.get')
    def test_raises_exception_on_failed_request(self, mock_get, mock_get_variable):
        """
        Test that the main function raises a RequestException
        if the API request fails.
        """
        mock_get_variable.side_effect = lambda key: "mock_value"
        mock_get.side_effect = requests.RequestException("Request failed")
        with self.assertRaises(requests.RequestException):
            main("/endpoint")


if __name__ == '__main__':
    unittest.main()
