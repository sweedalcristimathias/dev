
import json
import os

def load_book_data(file_path):
    """
    Load book data from a JSON file.

    Args:s
    - file_path (str): The path to the JSON file containing book data.

    Returns:
    - dict: A dictionary containing the loaded book data.
    """
    if os.path.exists(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            print('Error while reading file:', e)
            return {}
    else:
        return {}  # Return an empty dictionary directly for nonexistent files

def search_books_by_year(data, publication_year):
    """
    Search for books by publication year in the provided data.

    Args:
    - data (dict): A dictionary containing book data.
    - publication_year (int): The publication year to search for.
    """
    if 'books' in data:
        found_books = [book['Title'] for book in data['books'] if book['publication_Year'] == publication_year]
        if found_books:
            print("Books published in", publication_year, ":")
            for book in found_books:
                print("-", book)
        else:
            print("No books found for the entered publication year.")
    else:
        print("No books found in the data.")

def get_publication_year():
    """
    Prompt the user to enter a publication year.

    Returns:
    - int: The publication year entered by the user.
    """
    publication_year = input("Enter a publication year: ")
    
    try:
        return int(publication_year)
    except ValueError:
        print("Please enter a valid year.")
        return None

def main():
    file_path = "pythonproblems/books/books.json"
    data = load_book_data(file_path)
    
    if data:
        total_books = len(data.get('books', []))
        print(f"Total number of books: {total_books}")
        search_books_by_year(data, get_publication_year())

if __name__ == "__main__":
    main()
