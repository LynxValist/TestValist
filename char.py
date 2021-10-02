from luck import chance as lc
class Character():
    def __init__(self, n):#n=name REQURES NAME VARIABLE AND LEVEL
        self.name = str(n)
        self.maxhealth = 35.0
        self.health = self.maxhealth
        self.healthstats = 0
        self.attack = 7.0
        self.attackstats = 0
        self.defense = 2.0
        self.defensestats = 0
        self.accuracy = 90
        self.critical = 11
        self.victories = 0
        self.baseattack = self.attack
        self.basedef = self.defense
        self.statpoints = 0
    def PlayAttack(self): #PLAYER ATTACK HIT OR MISS + DAMAGE
        hit = lc.Percent(Character,self.accuracy)
        crit = lc.Percent(Character,self.critical)
        if hit == True and crit:
            return self.attack*2.5
        elif hit == True:
            return self.attack
        return 0
    def win(self):
        self.victories +=1
        self.statpoints += 3
        self.health = self.maxhealth
    def spendstats(self):
        print("Health Stat:", self.healthstats)
        print("Attack Stat:", self.attackstats)
        print("Defense Stat:", self.defensestats)
        q = True
        while q and self.statpoints != 0:   
            proceed = input("Do you wish to use your stat points?(q to quit): ")
            if proceed.lower() == "q":
                q = False
            elif proceed.lower() == "yes" and self.statpoints>0:
                print("1 for Health, 2 for Attack, 3 for Defense, and q to Quit!")
                while self.statpoints>0:
                    print("You have", self.statpoints,"statpoints!")
                    try:
                        choice = input("\n")
                        if choice == 'q':
                            break
                        elif int(choice) == 1:
                            self.healthstats +=1
                            self.statpoints-=1
                            print("You have successfully added a statpoint into health!")
                        elif int(choice) == 2:
                            self.statpoints-=1
                            self.attackstats +=1
                            print("You have successfully added a statpoint into attack!")
                        elif int(choice) == 3:
                            self.statpoints-=1
                            self.defensestats +=1
                            print("You have successfully added a statpoint into defense!")
                    except (TypeError, ValueError) as e:
                        print("Please enter q or an integer!")
                        
                    else:
                        print("Please try again later!")
            self.buffer()
    def buffer(self):
        self.maxhealth = round((self.healthstats*0.10)*35.0) + self.health
        self.attack = round((self.attackstats*0.15)*7.0) + self.baseattack
        self.defense = round((self.defensestats*0.12)*2.0) + self.basedef

    def DisplayStats(self):
        print("Name:", self.name)
        print("Health:", self.maxhealth)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Accuracy:", self.accuracy,"%")


class SideChar(): #ENEMIES/OPPONENTS
    def __init__(self, char_name, dungeonlvl):
        self.name = str(char_name)
        lis = [1,2,3]
        upg = []
        for i in range(dungeonlvl):
            upg.append(lc.listran(SideChar, lis))
        self.maxhealth = float(lc.rint(SideChar, 40,8))
        self.attack = float(lc.rint(SideChar,7,3))
        self.defense = float(lc.rint(SideChar,3,1))
        self.accuracy = 75
        for i in upg:
            if i == 1:
                self.maxhealth= round(self.maxhealth*1.5)
            elif i ==2:
                self.attack = round(self.attack*1.4)
            else:
                self.defense = round(self.defense*1.4)
        self.health = self.maxhealth
    def EnAttack(self): #ATTACK simulation
        hit = lc.Percent(SideChar,self.accuracy)
        if hit == True:
            return self.attack
        return 0
    def DisplayStats(self):
        print("Name:", self.name)
        print("Health:", self.health)
        print("Attack:", self.attack)
        print("Defense:", self.defense)
        print("Accuracy:", self.accuracy,"%")
    #def Guard(self):
        #return round(self.defense*1.5) #ACTIVE DEFENSE
