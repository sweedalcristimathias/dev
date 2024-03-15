Prerequisites

    - Python 3.x
    - JSON module (included in Python standard library)

Description 

    This project contains solutions to 3 Python problems.
    It provides a unified interface for users to understand and interact with the solutions.
    Unit tests are included for each problem solution.

Usage 

    Clone the repository.
    Navigate to the project directory.
    Run the main script for each problem.
    
Problem 1

    Book Search Application

        This Python project provides the functionality to load book data from a JSON file, search for books by publication year, and prompt users to enter a publication year for searching.

    Functionality

        search_books_by_year(data, publication_year):This function validates the year and returns the title of the book published in that year.

        get_publication_year():This function prompts the user to enter a year and checks if it's a valid year or not.

        main():This function returns the length of the books and also runs the search_books_by_year and get_publication_year.

    Run the main python script and the test script
    
        python books.py
        python booktest.py
    

Problem 2

    Date Validator

        This Python script provides functionality to validate dates in the format "YYYY-MM-DD". It checks whether the input date is a valid date or not.

    Functionality

        validate_date(date_str):This function validates the input valid date against a regular expression pattern representing the date format. It returns True if the date is valid, otherwise False.

        main(): This function prompts the user to enter a date and validates it using the validate_date() function. It then prints whether the entered date is valid or not.

    Run the main python script and the test script
        
        python date.py
        python datetest.py      

Problem 3

    Email Validator

        This Python script provides functionality to validate email addresses. It checks whether the input email address works according to the logic provided..

    Functionality

        valid_email(email): This function validates the input email address against a regular expression pattern representing the standard email format. It returns True if the email address is valid, otherwise False.

        main(): This function prompts the user to enter an email address and validates it using the valid_email() function. It then prints whether the entered email address is valid or not.

    Run the main python script and the test script
        
        python email.py
        python emailtest.py  