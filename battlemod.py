
class battlepassive():
    def recover(self, maxhealth, guard = False, status = None): #REQUIRES MAXIMUM HEALTH, Possible guard state, (not yet)status effects
        rec = 0.01*maxhealth
        if guard == True:
            return rec*3
        return rec
        #returns health recovered, not the entire health
    def battlecheck(self, health): #REQUIRES BATTLE HEALTH
        if health<=0:
            return False
        return True
    def display_health(self, health): #REQUIRES BATTLE HEALTH
        health = round(health)
        return str(health)

