import unittest
import main
object = main.Restaurant

class TestAdd(unittest.TestCase):
     def test_1(self):
         object.topthree(self, './src/main/eaterlog.csv', './src/main/foodmenu.csv')

     def test_2(self):
         object.topthree(self, './src/main/eaterlog1.csv', './src/main/foodmenu.csv')

if __name__ == '__main__':
    unittest.main()