import unittest

from windmill.f.flows.sync_work_packages__flow.inline_script_1 import main


class TestMainFunction(unittest.TestCase):
    def test_returns_href_when_present(self):
        input_dict = {
            "_links": {
                "workPackages": {
                    "href": "https://example.com/workPackages/123"
                }
            }
        }
        expected = "https://example.com/workPackages/123"
        self.assertEqual(expected, main(input_dict))

    def test_returns_none_when_missing_workPackages(self):
        input_dict = {
            "_links": {}
        }
        self.assertIsNone(main(input_dict))

    def test_returns_none_when_missing_links(self):
        input_dict = {}
        self.assertIsNone(main(input_dict))

    def test_returns_none_when_input_is_empty(self):
        input_dict = {}
        self.assertIsNone(main(input_dict))

    def test_returns_none_when_href_is_missing(self):
        input_dict = {
            "_links": {
                "workPackages": {}
            }
        }
        self.assertIsNone(main(input_dict))


if __name__ == "__main__":
    unittest.main()
