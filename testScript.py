import unittest
from main import BlackScholes

class TestBlackScholes(unittest.TestCase):
    def testAtMoneyCall(self):
        s = 100
        x = 100
        r = 0.05
        t = 0.5
        o = 0.3

        knownCallPrice = 9.63488

        model = BlackScholes(s, x, r, t, o)

        callPrice = model.mainFormula()

        self.assertAlmostEqual(knownCallPrice, callPrice, places = 5)


    def testInMoneyCall(self):
        s = 110
        x = 100
        r = 0.05
        t = 0.5
        o = 0.3
        
        knownCallPrice = 16.36545

        model = BlackScholes(s, x, r, t, o)

        callPrice = model.mainFormula()

        self.assertAlmostEqual(knownCallPrice, callPrice, places = 5)

if __name__ == '__main__':
    unittest.main()
