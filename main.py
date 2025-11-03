import math

class BlackScholes:
    # s = stock price
    # x = exercise price
# r = risk-free interest rate
# t = time to experation
# o = standerd deviation of log returns or (volitility)

    def __init__(self):
        self.s = input("Please Enter The Stock Price: ")
        self.x = input("Please Enter The Exercise Price: ")
        self.r = input("Please Enter The Risk-Free interest Rate:")
        self.t = input("Please Enter The Time to Experation: ")
        self.o = input("Please Enter The Standerd deviation: ")


    def mainFormula(self):
        d1 = self.d1(s, x, r, t, o)
        d2 = self.d2(d1)
        c = s * self.N(d1) - x * (math.e**(-r * t)) * self.N(d2)
    def N(self, x): #N(x) from the formula
        pass

    def d1(self, s, x, r, t, o):
        return (math.log(s/x) + (r + (o**2)/2))/(o * math.sqrt(t))

    def d2(self, d1):
        return d1 - (0 * math.sqrt(t))

obj = BlackScholes()
obj.mainFormula()
