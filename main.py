from luck import chance as lc
import char as ch
from battlemod import battlepassive as bp
#LIST VAR
quotes=["As you enter the first dungeon, you hear a strange noise.",
"On the second floor, you see a spooky sight.",
"When you enter the third floor, you feel a slight breeze on the back of your neck.",
"As you approach the fourth floor, your heart begins to beat faster.",
"Peeking into the fifth floor, you see something truly horrid!",
"Creeping behind you as you walk into the sixth floor, you turn around to see your worst nightmare.",
"You get a ominous feeling about the seventh floor, yet you still choose to enter.",
"As you enter the eighth floor, you begin to feel Deja vu","The ninth floor reeks!",
"As you look into the tenth and final floor, you see the face of death itself. You begin to wonder if this was a good idea and if you should just turn around, however, your thirst for gold and glory tells you otherwise and you choose to proceed."]
 
monsterlibrary = ["Raging Bear","Skeleton","Phantom","Zombie","Feral Wolf"]
 
endquotes=["Nice Job! looks like its time for the second floor.",
"Great victory! Time for round three.",
"Awesome! Fourth one upcoming.",
"Sweet! You really handled them. Move onto the fifth floor.",
"Epic. Head over to the sixth floor",
"Sick! Seventh floor is right around the corner",
"That was pretty rad! skrt over to the eighth floor",
"You really showed them who's boss.  You're almost there. Ninth floor!",
"Time for the final fight. Can you taste the gold?",
"Victory is yours. Thank you so much for clearing these monsters for me. Oh yeah! You must be wondering who's voice this is. It's me, Ered. Thank you so much for your generous donation. I'll tell ya what. I get 70 percent, and you get 30. Seems fair! "]
#INTRO
name = input("What is your name: ")
player = ch.Character(name)
print("Erid: Welcome " + name + " to the mysterious dungeon of Vanity!")
print("Erid: I am Erid, a fisherman from a nearby town. I see that you are here to explore this dungeon. Legends say that King Midas' lost treasure is at the end of the dungeon. Unfortunately, nobody has ever come out alive. They say that those who die in the dungeon serve as its protectors. This is a very dangerous journey.")
readiness = 0
#TEST1
while True:
  ready = input("Erid: Are you sure you want to continue?: ")
  if ready.lower() == "yes":
      print("Erid: I wish you the best of luck " + name + "!" )
      readiness = 1
      break
  elif ready.lower() == "no":
      print("Erid: Come again when you are ready. I'm sure a strong traveler like you will be able to accomplish great things!")
      break
if readiness != 1:
  print("Game Over!")
  exit()
print("As you enter the first dungeon, you hear a strange noise")
#Battles __ HERE
while player.victories!=10:
   print("Type s to view status. Type z to leave.")
   print("When you are ready to move on, type continue")
   action = input("")
   if ((action.lower() == 'continue') or (action.lower() == 'c')):
       print(quotes[player.victories])
       monstername = lc.listran(1, monsterlibrary)
       dungeon = ch.SideChar(monstername, 2*player.victories)
       dungeon.DisplayStats()
       not_dead = True
       playerguard = False
       monsterguard = False
       def turnreset():
           playerguard = False
           monsterguard = False
           dungeon.health = dungeon.health + bp.recover(bp,dungeon.maxhealth,monsterguard)
         if dungeon.health>dungeon.maxhealth:
             dungeon.health = dungeon.maxhealth
       while not_dead:
       #player action
           move = input("Attack or Defend: ")
           if (move.lower() == ("attack") or move.lower() == ("a")):
               atk = player.PlayAttack()
               dfs = dungeon.defense
               if monsterguard:
                   dmg = round(atk-dfs*3)
                   print("O The", monstername, "has defended! ")
               else:
                   dmg = atk-dfs
               if dmg<0:
                   dmg=0
               dungeon.health -= dmg
               print("---You Attacked!---\n---You dealt", dmg, "damage!---")
               print("---",monstername, "has",round(dungeon.health),"health remaining!---")
               if bp.battlecheck(dungeon, dungeon.health):
                   pass
               else:
                   break
           elif (move.lower() == ("defend") or move.lower() == ("d")):
               print("---You are on Guard!---")
               playerguard = True
           else:
               continue
           monsterguard = False
           #monster action
           if lc.Fraction(dungeon,4,5):
               atk = dungeon.EnAttack()
               dfs = player.defense
               if playerguard:
                   dmg = round(atk-dfs*3)
                   print("---You defended!---")
               else:
                   dmg = atk-dfs
               if dmg<0:
                   dmg = 0
               player.health -= dmg
               print("O The", monstername, "attacked! \nO", monstername,"dealt",dmg,"damage! ")
               print("O You have", round(player.health)," health remaining!")
           else:
               monsterguard = True
               print("O", monstername, "is on guard! ")
           if bp.battlecheck(player, player.health):
               pass
           else:
               not_dead = False
               print("Battle is over!")
           turnreset()
       if player.health<0:
           a = input("Game Over!")
           exit()
       else:
         player.health = player.maxhealth
         print(endquotes[player.victories])
         player.win()
         print(monstername + " was defeated!")
         player.spendstats()
   elif action.lower() == "s":
       player.DisplayStats()
   elif action.lower() == "z":
       exit()
   else:
       pass
      
if player.victories == 10:
 print("You win! End of Game.")
 
 
 
 

