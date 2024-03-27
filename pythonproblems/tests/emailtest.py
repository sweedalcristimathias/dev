from unittest.mock import patch, MagicMock
import unittest
import sys
sys.path.insert(1, r'pythonproblems/datecheck')
from email import valid_email

class TestDateValidator(unittest.TestCase):

    def test_valid_email(self):
        with open('tests/mocks/valid_email.txt', 'r') as file: 
            valid_emails = file.readlines()
        
        for email_str in valid_emails:
            with patch('builtins.input', side_effect=[email_str.strip()]):
               
                result = valid_email(email_str)
                
                self.assertTrue(result,f"Expected '{email_str.strip()}' to be a valid email")

    def test_invalid_email(self):
        with open('tests/mocks/invalid_email.txt', 'r') as file:
            invalid_emails = file.readlines()
        
        for email_str in invalid_emails:
            with patch('builtins.input', side_effect=[email_str.strip()]):
                
                result = valid_email(email_str)
                
                self.assertFalse(result,f"Expected '{email_str.strip()}' to be an invalid email")

if __name__ == "__main__":
    unittest.main()








