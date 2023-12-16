import unittest
from code.string_calculator import add

class FourthTestCases(unittest.TestCase):
    def test_basic_string(self):
        result = add("//,\n1,2,3")
        self.assertEqual(result, 6)
        
    def test_complex_string(self):
        result = add("//,\n21,45,3,0,12")
        self.assertEqual(result, 81)
    
    def test_wrong_delimeter(self):
        result = add("//,\n21;45;3;0;12")
        self.assertEqual(result, 'Error, string not correctly formatted')
        
    def test_empty_string(self):
        result = add("//,\n")
        self.assertEqual(result, 0)
        
    def test_mixed_delimeters_string(self):
        result = add("21\n 0, 15\n 1, 0")
        self.assertEqual(result, 'Error, string not correctly formatted')
        
    def test_wrong_delimeters_tail_string(self):
        result = add("21, 0, 15, 1, 0\n,")
        self.assertEqual(result, 37)
    
    def test_wrong_delimeters_string(self):
        result = add("21* 0 *, 15\n 1) 0")
        self.assertEqual(result, 'Error, string not correctly formatted')
        
    def test_negative_basic_string(self):
        result = add("//,\n1,2,-3")
        self.assertEqual(result, 'Negatives not allowed : -3')
        
    def test_multiple_negatives(self):
        result = add("//,\n21,-45,3,0,-12")
        self.assertEqual(result, 'Negatives not allowed : -45, -12')
        
        
if __name__ == '__main__':
    unittest.main()
    input("Premi Enter per chiudere la console...")