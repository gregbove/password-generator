import unittest
from generator.exception_messages import STRING_CAN_NOT_BE_NULL_OR_EMPTY
from generator.string_helpers import get_first_x, calculate_hash

class test_string_helpers(unittest.TestCase):

    # ----- get_first_x ------

    def test_get_first_zero(self):
        result = get_first_x("hello", 0)
        self.assertEqual(result, "")

    def test_get_first_x_standard(self):
        result = get_first_x("hello", 3)
        self.assertEqual(result, "hel")

    def test_get_full_length(self):
        result = get_first_x("hello", 5)
        self.assertEqual(result, "hello")

    def test_get_more_than_full_length(self):
        result = get_first_x("hello", 10)
        self.assertEqual(result, "hello")

    def test_empty_string(self):
        result = get_first_x("", 5)
        self.assertEqual(result, "")

    # ----- calculate_hash ------

    def test_hash_standard(self):
        result = calculate_hash("Hello, World!")
        self.assertEqual(result, "dffd6021bb2bd5b0af676290809ec3a53191dd81c7f70a4b28688a362182986f")

    def test_hash_blank_string(self):
        with self.assertRaises(Exception) as context: 
            calculate_hash("")
        self.assertEqual(str(context.exception), STRING_CAN_NOT_BE_NULL_OR_EMPTY)

if __name__ == '__main__':
    unittest.main()
