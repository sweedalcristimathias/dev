import re

def validate_date(date_str):
    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(pattern, date_str):
        year, month, day = map(int, date_str.split('-'))
        if 1 <= month <= 12 and 1 <= day <= 31:
            if month in [4, 6, 9, 11]:
                return 1 <= day <= 30
            elif month == 2:
                if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                    return 1 <= day <= 29
                else:
                    return 1 <= day <= 28
            else:
                return True
    return False

def main():
    date_str = input("Enter a date (YYYY-MM-DD): ")
    if validate_date(date_str):
        print("Valid date")
    else:
        print("Invalid date")

if __name__ == "__main__":
    main()


