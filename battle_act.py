from Battle_mod import battlepassive as bp
from luck import chance as lc
not_dead = True
playerguard = False
monsterguard = False

def turnreset():
    playerguard = False
    mons.health = mons.health + bp.recover(mon.maxhealth,monsterguard)
    if mons.health>mon.health:
        mons.health = mon.health

while not_dead:
    #player action
    if input == attack:
        atk = game.Character.PlayAttack()
        dfs = game.mon.Defend()
        if monsterguard:
            dmg = round(atk-dfs*1.5)
        else:
            dmg = atk-dfs
        if dmg<0:
            dmg=0
        mons.health = mons.health-dmg
    elif input == guard:
        playerguard = True

    monsterguard = False

    #monster action
    if lc.Fraction(4,5):
        atk = game.mon.MonAttack()
        dfs = game.Character.Defend()
        if playerguard:
            dmg - round(atk-dfs*1.5)
        else:
            dmg = atk-dfs
        if dmg<0:
            dmg = 0
        Character.health = Character.health - dmg
    else:
        monsterguard = True

    

    if bp.battlecheck(mons.health) and bp.battlecheck(character.health):
        pass
    else:
        not_dead = False
    turnreset()
#battle ends
#health check at the end to determine victor        
