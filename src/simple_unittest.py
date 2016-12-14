import unittest
import myCalc

class MycalcTest(unittest.TestCase):
    
    def test_add(self):
        c = myCalc.add(20,10)
        self.assertEqual(c, 30)
    def test_substract(self):
        c = myCalc.substract(20,10)
        self.assertEqual(c, 110)   
        
if __name__ == '__main__':
    unittest.main()
    