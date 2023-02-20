from customers.utils import is_cpf_valid
import unittest

# These tests are just for testing 
# the 'is_cpf_valid' function present
# in utils.py


class TestCpf(unittest.TestCase):
     
    def test_valid_str_only_numbers_cpf(self):
        cpf = "83227151022"
        self.assertTrue(is_cpf_valid(cpf))
    
    def test_valid_str_with_mask_cpf(self):
        cpf = "196.527.200-20"
        self.assertTrue(is_cpf_valid(cpf))
        
    def test_valid_int_cpf(self):
        cpf = 97492727062
        self.assertTrue(is_cpf_valid(cpf))
    
    def test_invalid_str_mask_cpf(self):
        cpf = "449.976.980-32" # Valid: 449.976.980-91
        self.assertFalse(is_cpf_valid(cpf))
        
    def test_invalid_str_only_numbers_cpf(self):
        cpf = "27717074000" # Valid: 27717074036
        self.assertFalse(is_cpf_valid(cpf))
        
    def test_invalid_int_cpf(self):
        cpf = 97492727032 # Valid: 97492727062
        self.assertFalse(is_cpf_valid(cpf))
    
    def test_invalid_size_str_mask_cpf(self):
        cpf = "277.170.740-362" # Invalid Size
        self.assertFalse(is_cpf_valid(cpf))
        
    def test_invalid_size_str_only_numbers_cpf(self):
        cpf = "7726670509643" # Invalid size
        self.assertFalse(is_cpf_valid(cpf))
        
    def test_invalid_size_int_cpf(self):
        cpf = 97492727062451 # Invalid size
        self.assertFalse(is_cpf_valid(cpf))
        
    def test_invalid_characters_in_cpf(self):
        cpf = "25##%013037"
        self.assertFalse(is_cpf_valid(cpf))