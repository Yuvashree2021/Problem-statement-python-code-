import unittest
import main
object = main.Restaurant

class TestAdd(unittest.TestCase):
     def test_1(self):
         object.topthree(self, './eaterlog.csv', './foodmenu.csv')

     def test_2(self):
         object.topthree(self, './eaterlog1.csv', './foodmenu.csv')

if __name__ == '__main__':
    unittest.main()