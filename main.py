print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload


answer = input("What\'s do you think, where is the island? \'Left\' or \'Right\' \'L\'/\'R\'?").lower()

if (answer == "l") or (answer == "left"):
  answer = input("You can choose the left or the right door? Left or Right L/R").lower()
  if (answer == "l") or (answer == "left"):
    answer = input("You have to swim or to walk over the mountain. What do you decide for? \"Swim\" or \"Walk\"?").lower()
    if (answer == "swim") or (answer == "s"):
      answer = input("There are three doors, wich one do you choose? The blue, \"red\" or \"yellow\" one?").lower()
      if (answer == "b") or (answer == "blue"):
        print("You are burned by fire. Game Over").lower()
      elif (answer == "r") or (answer == "red"):
        print("You are eaten by beasts. Game Over")
      else:
        print("You won the game, congratulation! ;-) ")
    else:
      print("Wrong decission. Game Over")
  else:
    print("It is the other door. Game Over")
else:
  print("You fell into a hole. Game Over.")



print('''
                                           _L/L
                                         _LT/l_L_
                                       _LLl/L_T_lL_
                   _T/L              _LT|L/_|__L_|_L_
                 _Ll/l_L_          _TL|_T/_L_|__T__|_l_
               _TLl/T_l|_L_      _LL|_Tl/_|__l___L__L_|L_
             _LT_L/L_|_L_l_L_  _'|_|_|T/_L_l__T _ l__|__|L_
           _Tl_L|/_|__|_|__T _LlT_|_Ll/_l_ _|__[ ]__|__|_l_L_
    jjs_ _LT_l_l/|__|__l_T _T_L|_|_|l/___|__ | _l__|_ |__|_T_L_  __

                           nn_r   nn_r                 __
                     __   /l(\   /l)\      nn_r
               __                         /\(\    __
''')

