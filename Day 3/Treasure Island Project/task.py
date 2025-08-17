print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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
first_decision = input("You reach to the fork, please decide left or right ")
if first_decision.lower() == "left":
    print("You found a right way!")
    second_decision = input("you found the small river while on the way. will you swim? or wait ")
    if second_decision.lower() == "wait":
        print("water drained! you can cross the river")
        third_decision = input("You arrive at the island unharmed."
                               "There is house with 3doors. One red,"
                               "One Yellow and one blue. "
                               "Which color do you choose?").lower()
        if third_decision =="red":
            print("It's a room full of fire. Game over")
        elif third_decision =="yellow":
            print("You found the treasure. You Win!")
        elif third_decision =="blue":
            print("you enter a room of  beasts. Game over!")
        else:
            print("You choose a door that doesn't exist. Game Over")
    else:
        print(r'''               ,
             .';
         .-'` .'
       ,`.-'-.`\
      ; /     '-'
      | \       ,-,
      \  '-.__   )_`'._
       '.     ```      ``'--._
      .-' ,                   `'-.
       '-'`-._           ((   o   )
              `'--....(`- ,__..--'
                       '-'`''')
        print("You get eaten by a shark ")
else:
    print(r'''            
                        _,.--.
    --..,_           .'`__ o  `;__,
       `'.'.       .'.'`  '---'`  '         
          '.`-...-'.'
            `-...-'
''')
    print("Snake bite you. Game Over")
# third_decision = input("Finally you reach to the end. you have to choose a door. There three doors in front of you \n Red, Yellow, Blue")