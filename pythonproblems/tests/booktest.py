import unittest
from unittest.mock import patch
from io import StringIO
import json
import os
import sys

# Import the functions to be tested
sys.path.insert(1,r'pythonproblems/books/books.py')
from books import load_book_data, search_books_by_year, get_publication_year

class TestBookFunctions(unittest.TestCase):
    def setUp(self):
        # Create a mock JSON file for testing
        self.test_data = {
            "books": [
                {"Title": "Book 1", "Publication_Year": 1900},
                {"Title": "Book 2", "Publication_Year": 2000},
                {"Title": "Book 3", "Publication_Year": 2001}
            ]
        }
        with open("mock_books.json", "w") as file:
            json.dump(self.test_data, file)

    def tearDown(self):
        # Remove the mock JSON file after testing
        os.remove("mock_books.json")

    def test_load_book_data_existing_file(self):
        loaded_data = load_book_data("mock_books.json")
        self.assertEqual(loaded_data, self.test_data)

    def test_load_book_data_nonexistent_file(self):
        loaded_data = load_book_data("nonexistent_file.json")
        self.assertEqual(loaded_data, {})

    @patch('builtins.input', side_effect=["2000"])  # Mock user input
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_books_by_year_found(self, mock_stdout, mock_input):
        search_books_by_year(self.test_data, 2000)
        expected_output = "Books published in 2000 :\n- Book 1\n- Book 2\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["1999"])  # Mock user input
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_books_by_year_not_found(self, mock_stdout, mock_input):
        search_books_by_year(self.test_data, 1999)
        expected_output = "No books found for the entered publication year.\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', side_effect=["invalid_year", "2000"])  # Mock user input
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_books_by_year_invalid_input(self, mock_stdout, mock_input):
        search_books_by_year(self.test_data, 2000)
        expected_output = "Please enter a valid year.\nBooks published in 2000 :\n- Book 1\n- Book 2\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == '__main__':
    unittest.main()
