import random
import sys



Suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"]

Values = ["ACE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING"]

Cards = []

Hand = []

Table = []

EndGame = []

for item in Suits:
    for item1 in Values:
        Cards.append(str(item1) + " OF " + str(item))

for x in range(2):
    rand = random.randint(1,len(Cards))

    Hand.append(Cards[rand])

    Cards.remove(Cards[rand])

print ("Your hand contains the \n")
for item in Hand:
    print (item)
print ()

for x in range(3):
    rand = random.randint(1,len(Cards))

    Table.append(Cards[rand])

    Cards.remove(Cards[rand])

print ("The flop contains the: \n" )
for item in Table:
    print (item)
print ()

"""Turn1 = input("Do you bet, check, or fold?  ")
Turn1 = Turn1.lower()
Turn1 = Turn1.replace(" ", "")

if Turn1 == "bet":
    bet1 = int(input("\nHow much do you bet?  "))

elif Turn1 == "check":
    bet1 = 0

elif Turn1 == "fold":
    print ("Round over")
    sys.exit()
    
else:
    print ("Not an acceptable answer")
    print ("Checking instead")
    bet1 = 0"""

for x in range(1):
    rand = random.randint(1,len(Cards))

    Table.append(Cards[rand])

    Cards.remove(Cards[rand])

print ("The turn contains the: \n")
print (str(Table[3]))

"""Turn2 = input ("\nDo you bet, check, or fold?  ")
Turn2 = Turn2.lower()
Turn2 = Turn1.replace(" ", "")

if Turn2 == "bet":
    bet2 = int(input("\nHow much do you bet?  "))

elif Turn2 == "check":
    bet2 = 0

elif Turn2 == "fold":
    print ("\nRound over")
    sys.exit()

else:
    print ("Not an acceptable answer")
    print ("Checking instead")
    bet2 = 0"""

for x in range(1):
    rand = random.randint(1,len(Cards))

    Table.append(Cards[rand])

    Cards.remove(Cards[rand])

print ("\nThe river contains the: \n")
print ((Table[4]))

"""Turn3 = input ("\nDo you bet, check, or fold?  ")
Turn3 = Turn2.lower()
Turn3 = Turn1.replace(" ", "")

if Turn3 == "bet":
    bet3 = int(input("\nHow much do you bet?  "))

elif Turn3 == "check":
    bet3 = 0

elif Turn2 == "fold":
    print ("\nRound over")
    sys.exit()

else:
    print ("Not an acceptable answer")
    print ("Checking instead")
    bet3 = 0

Totbet = bet1 + bet2 + bet3"""

print ("- - - - - - - - - - - - ")
print ()

for item in Table:
    Hand.append(item)

for item in Hand:
    split = item.split(" ")
    EndGame.append(split[0])
    EndGame.append(split[2])

for item in Suits:
    count = 0
    if item in EndGame:
        count += 1

    if count == 5:
        print ("Flush")
        sys.exit()

for item in Values:
    count = 0

    for items in EndGame:
        if item == items:
            count += 1

    if count == 2:
        print ("Pair of " + str(item) + 'S')

    if count == 3:
        print ("Three of a kind of " + str(item) + 'S')

    if count == 4:
        print ("Four of a kind of " + str(item) + 'S')



""" To do

-Add all the hands


-For Straights, use dict (Ace:1), order hand, if set of five has an average
equal to the third value, then call it a straight

"""



        
        
           

        

        




    






    


