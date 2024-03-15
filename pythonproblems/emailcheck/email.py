import re

def valid_email(email):
    pattern = r'^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def main():
    email = input("Enter an email address: ")
    if valid_email(email):
        print("Valid email address.")
    else:
        print("Invalid email address.")

if __name__ == "__main__":
    main()