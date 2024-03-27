from unittest.mock import patch, MagicMock
import unittest
import sys
sys.path.insert(1, r'C:\Users\SweedalMathias\Desktop\angularproject\pythonproblems\datecheck')
from .date import validate_date

class TestDateValidator(unittest.TestCase):

    def test_valid_dates(self):
        with open('tests/mocks/valid_dates.txt', 'r') as file: 
            valid_dates = file.readlines()
        
        for date_str in valid_dates:
            with patch('builtins.input', side_effect=[date_str.strip()]):
                
                result = validate_date(date_str)
               
                self.assertTrue(result,f"Expected '{date_str.strip()}' to be a valid date")

    def test_invalid_dates(self):
        with open('tests/mocks/invalid_dates.txt', 'r') as file:
            invalid_dates = file.readlines()
        
        for date_str in invalid_dates:
            with patch('builtins.input', side_effect=[date_str.strip()]):
                
                result = validate_date(date_str)
                
                self.assertFalse(result,f"Expected '{date_str.strip()}' to be an invalid date")

if __name__ == "__main__":
    unittest.main()

























# from unittest.mock import patch, MagicMock
# import unittest
# import sys
# sys.path.insert(1, r'C:\Users\SweedalMathias\Desktop\angularproject\pythonproblems\datecheck')
# from date import validate_date

# class TestDateValidator(unittest.TestCase):

#     def test_valid_dates(self):
#         with open('tests/mocks/valid_dates.txt', 'r') as file: 
#             valid_dates = file.readlines()
        
#         for date_str in valid_dates:
#             with patch('builtins.input', side_effect=[date_str.strip()]):
                
#                 result = validate_date(date_str)
               
#                 self.assertTrue(result,f"Expected '{date_str.strip()}' to be a valid date")

#     def test_invalid_dates(self):
#         with open('tests/mocks/invalid_dates.txt', 'r') as file:
#             invalid_dates = file.readlines()
        
#         for date_str in invalid_dates:
#             with patch('builtins.input', side_effect=[date_str.strip()]):
                
#                 result = validate_date(date_str)
                
#                 self.assertFalse(result,f"Expected '{date_str.strip()}' to be an invalid date")

# if __name__ == "__main__":
#     unittest.main()








