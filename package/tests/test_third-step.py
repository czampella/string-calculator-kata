import unittest
from code.string_calculator import add

class ThirdTestCases(unittest.TestCase):
    def test_basic_string(self):
        result = add("1\n2\n3")
        self.assertEqual(result, 6)
        
    def test_empty_string(self):
        result = add("\n")
        self.assertEqual(result, 0)
        
    def test_mixed_delimeters_string(self):
        result = add("21\n 0, 15\n 1, 0")
        self.assertEqual(result, 37)
        
    def test_wrong_delimeters_tail_string(self):
        result = add("21, 0, 15, 1, 0\n,")
        self.assertEqual(result, 37)
    
    def test_wrong_delimeters_string(self):
        result = add("21* 0 *, 15\n 1) 0")
        self.assertEqual(result, 0)
        
        
if __name__ == '__main__':
    unittest.main()
    input("Premi Enter per chiudere la console...")