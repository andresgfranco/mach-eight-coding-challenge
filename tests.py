import unittest
from app import find_pairs_sum

class FindPairsSumTestCase(unittest.TestCase):
    def test_positive_case_with_multiple_pairs(self):
        numbers_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        target_sum = 110
        expected_result = {(10, 100), (20, 90), (30, 80), (40, 70), (50, 60)}
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

    def test_list_with_negative_numbers(self):
        numbers_list = [-1, 2, -3, 4, -5]
        target_sum = -1
        expected_result = {(-5, 4), (-3, 2)}
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

    def test_unsorted_list_with_positive_numbers(self):
        numbers_list = [5, 3, 2, 4, 1]
        target_sum = 6
        expected_result = {(1, 5), (2, 4)}
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

    def test_unsorted_list_with_positive_and_negative_numbers(self):
        numbers_list = [-5, 2, -3, 4, -1]
        target_sum = -1
        expected_result = {(-5, 4), (-3, 2)}
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

    def test_no_pairs_found(self):
        numbers_list = [1, 2, 3, 4, 5]
        target_sum = 10
        expected_result = "No pairs were found"
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

    def test_unsorted_list_with_no_pairs_found(self):
        numbers_list = [5, 4, 3, 2, 1]
        target_sum = 10
        expected_result = "No pairs were found"
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

    def test_empty_list(self):
        numbers_list = []
        target_sum = 5
        expected_result = "Wrong input. Please provide a list of two (or more) integers"
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

    def test_list_with_single_element(self):
        numbers_list = [5]
        target_sum = 5
        expected_result = "Wrong input. Please provide a list of two (or more) integers"
        self.assertEqual(find_pairs_sum(numbers_list, target_sum), expected_result)

if __name__ == '__main__':
    unittest.main()
