import math as m
from random import randint as ran, choice as ch

class chance():
    def Percent(self, per): #simulates percent chance REQUIRES PERCENT
        try:
            per = float(per)
            fac = ran(0, 1000)
        except TypeError:
            return False
        if fac <= per*10:
            return True
        return False
    def Fraction(self, id1, id2):  #fractional chance REQUIRES NUMERATOR and DENOMINATOR
        try:
            rin = ran(0,id2)
        except TypeError:
            return False
        if id1>=rin:
            return True
        return False
    def TruFal(self):  #return boolean 1/2 chance
        lis = [True, False]
        ans = ch(lis)
        return ans
    def listran(self, lis):  #random choice from list REQUIRES LIST
        anss = ch(lis)
        return anss
    def rint(self, num, fir = 0): #random integer REQUIRES MAXIMUM and POSSIBLE MINIMUM
        return ran(fir,num)

