
class battlepassive():
    def recover(self, health, guard = False, status = None): #REQUIRES MAXIMUM HEALTH, Possible guard state, (not yet)status effects
        health = 0.01*health
        if guard == True:
            return health*3
        return health
        #returns health recovered, not the entire health
    def battlecheck(self, health): #REQUIRES BATTLE HEALTH
        if health<=0:
            return False
        return True
    def display_health(self, health): #REQUIRES BATTLE HEALTH
        health = round(health)
        return str(health)

