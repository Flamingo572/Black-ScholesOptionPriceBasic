import math
from scipy.stats import norm

class BlackScholes:
    # s = stock price
    # x = exercise price
# r = risk-free interest rate
# t = time to experation
# o = standerd deviation of log returns or (volitility)

    def __init__(self, s, x, r, t, o):
        self.s = s
        self.x = x 
        self.r = r
        self.t = t
        self.o = o


    def mainFormula(self):
        d1 = self.d1(self.s, self.x, self.r, self.t, self.o)
        d2 = self.d2(d1)
        c = self.s * self.N(d1) - self.x * math.exp(-self.r * self.t) * self.N(d2)
        print("--Results--")
        print(f"d1: {d1:.6f}")
        print(f"d2: {d2:.6f}")
        print(f"Call Price: ${c:.2f}")
        return c

    def N(self, x): #N(x) from the formula
        return norm.cdf(x)

    def d1(self, s, x, r, t, o):
        return (math.log(s/x) + (r + (o**2)/2) * t)/(o * math.sqrt(t))

    def d2(self, d1):
        return d1 - (self.o * math.sqrt(self.t))

if __name__ == '__main__':
    obj = BlackScholes()
    obj.mainFormula()
