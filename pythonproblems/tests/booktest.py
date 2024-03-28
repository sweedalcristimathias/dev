import unittest
from unittest.mock import patch
from io import StringIO
import json
import os
import sys

# Adjust the path to include the correct directory containing the modules
sys.path.append(os.path.abspath('pythonproblems/books'))

# Import the functions to be tested
from books import load_book_data, search_books_by_year, get_publication_year

class TestBookFunctions(unittest.TestCase):
    def setUp(self):
        # Define a sample book data for testing
        self.sample_book_data = {
            "books":[
                {
                    "Title":"Book 1",
                    "Author":"Author 1",
                    "publication_Year":2000,
                    "ISBN":"978-1-23456-789-0"
                },
                {
                    "Title":"Book 2",
                    "Author":"Author 2",
                    "publication_Year":2020,
                    "ISBN":"978-1-23456-789-1"
                }
            ]
        }

    def test_load_book_data_existing_file(self):
        # Create a temporary file containing sample book data
        with open("sample_books.json", "w") as file:
            json.dump(self.sample_book_data, file)

        # Test loading book data from the temporary file
        loaded_data = load_book_data("sample_books.json")
        self.assertEqual(loaded_data, self.sample_book_data)

        # Remove the temporary file
        os.remove("sample_books.json")

    @patch('builtins.input', return_value="2020")  # Mock user input
    @patch('sys.stdout', new_callable=StringIO)
    def test_search_books_by_year_found(self, mock_stdout, mock_input):
        # Test searching for books published in 2020
        search_books_by_year(self.sample_book_data, 2020)
        expected_output = "Books published in 2020 :\n- Book 2\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    # @patch('builtins.input', return_value="invalid_year")  # Mock invalid user input
    # @patch('sys.stdout', new_callable=StringIO)
    # def test_search_books_by_year_invalid_input(self, mock_stdout, mock_input):
    #     # Test searching for books with invalid input
    #     search_books_by_year(self.sample_book_data, "invalid_year")
    #     expected_output = "Please enter a valid year.\n"
    #     self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('builtins.input', return_value="1990")  # Mock user input
    def test_get_publication_year_valid_input(self, mock_input):
        # Test getting a valid publication year from user input
        publication_year = get_publication_year()
        self.assertEqual(publication_year, 1990)

    @patch('builtins.input', return_value="invalid_year")  # Mock invalid user input
    def test_get_publication_year_invalid_input(self, mock_input):
        # Test getting an invalid publication year from user input
        publication_year = get_publication_year()
        self.assertIsNone(publication_year)

if __name__ == '__main__':
    unittest.main()
