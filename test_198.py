# test_198

import importlib
import unittest

# _198 = importlib.import_module("198 - Unittest")
_198 = importlib.import_module("15-testing.198-Unittest")

print(_198.do_stuff(5))  # 10
print(_198.do_stuff("10"))  # 15
print(_198.do_stuff("text"))  # None


# TODO: standard way to work with unittest
class TestMain(unittest.TestCase):  # inheriting TestCase class

    def setUp(self):  # setUp: run before each test
        print("starting test")

    def tearDown(self):  # tearDown: run after each test
        print("cleaning up")

    def test_with_integer(self):  # 10 + 5 = 15
        test_param = 10
        result = _198.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_with_string_number(self):  # '10' + 5 = 15
        test_param = "10"
        result = _198.do_stuff(test_param)
        self.assertEqual(result, 15)

    def test_with_invalid_string(self):  # 'text' + 5 = None
        test_param = "text"
        result = _198.do_stuff(test_param)
        self.assertEqual(result, None)

    # def test_with_invalid_string(self):             # 'text' + 5 = ValueError (raised)
    #     test_param = 'text'
    #     # with self.assertRaises(Exception):
    #     with self.assertRaises(ValueError):
    #         _198.do_stuff(test_param)

    # def test_with_invalid_string(self):             # 'text' + 5 = ValueError (instance)
    #     test_param = 'text'
    #     result = _198.do_stuff(test_param)
    #     self.assertTrue(isinstance(result, ValueError))
    #     self.assertIsInstance(result, ValueError)

    def test_with_none(self):  # None + 5 = 'please enter number'
        test_param = None
        result = _198.do_stuff(test_param)
        self.assertEqual(result, "please enter number")

    def test_with_empty_string(self):  # '' + 5 = 'please enter number'
        test_param = ""
        result = _198.do_stuff(test_param)
        self.assertEqual(result, "please enter number")


# TODO: run the test
if __name__ == "__main__":
    unittest.main()
else:
    print("test_198 was imported")
