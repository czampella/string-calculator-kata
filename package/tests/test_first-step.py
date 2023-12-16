import unittest
from code.string_calculator import add

class FirstTestCases(unittest.TestCase):
    def test_basic_string(self):
        result = add("1,2,3")
        self.assertEqual(result, 6)
        
    def test_empty_string(self):
        result = add("")
        self.assertEqual(result, 0)
        
    def test_improved_string(self):
        result = add("21, 0, 15, 1, 0")
        self.assertEqual(result, 37)
        
        
# if __name__ == '__main__':
#     unittest.main()
#     input("Premi Enter per chiudere la console...")