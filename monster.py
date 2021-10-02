from mon_name_lib import mon_n as mnl
from luck import chance as lc
import random as ran
mon_name = ran.choice(mnl)

class Monster(): #REQUIRES NAME and LEVEL OF PLAYER
    def __init__(self, mon_name, lvl):
        if lvl>3:
            hl = lc.TruFal(self) 
            add = lc.listran(self,[1,2,3])
            if hl == True:
                self.level = lvl+add
            elif hl == False:
                self.level = lvl-add
        else:
            self.level = lvl
        #pulls items out of library, on wait for kill to drop? possible feature (self.drops=list)
        self.name = str(mon_name)
        self.health = float(self.level*40+30)
        self.attack = self.level*3+2
        self.defense = self.level*1+2
        self.accuracy = 75+self.level
        if self.accuracy>100:
            self.attack+=(self.accuracy-100)
            self.accuracy = 100
    def MonAttack(self): #ATTACK simulation
        hit = lc.Percent(Monster,self.accuracy)
        if hit == True:
            return self.attack
        return 0
    def Defend(self): #PASSIVE DEFENSE
        return self.defense
    def Drop(self): #DROP RATE might not be implemented initially
        spina = lc.rint(Monster,5*self.level,self.level)
        exp = self.level*50
        return [exp, spina]
    #def Guard(self):
        #return round(self.defense*1.5) #ACTIVE DEFENSE
""" item drops? in a list?"""


""" example
r = Monster(mon_name,4)
print(r.Drop())
"""