import random
import sys
import time


def BlackJack():

    Suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"]
    Values = {"ACE" : 1, "TWO" : 2, "THREE" : 3, "FOUR" : 4, "FIVE" : 5, "SIX" : 6,
          "SEVEN" : 7, "EIGHT" : 8, "NINE" : 9, "TEN" : 10, "JACK" : 10,
          "QUEEN" : 10, "KING" : 10}

    def Hit(Bank, Cards, Hand):
        rand = random.randint(1,52)
        while rand not in Cards:
            rand = random.randint(1,52)
        Hand.append(Cards[rand])
        Bank.remove(Cards[rand][0])
        del Cards[rand]
        return Bank, Cards, Hand

    def Stay(Bank, Cards, Dealer):
        rand = random.randint(1,52)
        while rand not in Cards:
            rand = random.randint(1,52)
        Dealer.append(Cards[rand])
        Bank.remove(Cards[rand][0])
        del Cards[rand]
        return Bank, Cards, Dealer

    def Win(Dealer, DealerTotal):
        print ("The Dealer has a score of: " + str(DealerTotal) + '\n')
        print ("You Win. The Dealer shows: \n")
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return
    
    def Lose(Dealer, DealerTotal):
        print ("The Dealer has a score of: " + str(DealerTotal) + '\n')
        print ("You Lose. The Dealer shows: \n")
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return

    def WinWin(Dealer, DealerTotal):
        print ("The Dealer has a score of: " + str(DealerTotal) + '\n')
        print ("You Win both hands. The Dealer shows: \n")
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return

    def WinLose(Dealer, DealerTotal):
        print ("The Dealer has a score of: " + str(DealerTotal) + '\n')
        print ("You Win one hand. The Dealer shows: \n")
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return

    def LoseLose(Dealer, DealerTotal):
        print ("The Dealer has a score of: " + str(DealerTotal) + '\n')
        print ("You Lose both hands. The Dealer shows: \n")
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return
    
    def Bust():
        print ("You Bust")
        return
    
    def DealBust(Dealer, DealerTotal):
        print ("The Dealer Busts with a score of: " + str(DealerTotal) + '\n')
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return
    
    def Tie(Dealer, DealerTotal):
        print ("The Dealer has a score of: " + str(DealerTotal) + '\n')
        print ("The game is a Tie. The Dealer shows: \n")
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return
    
    def BlackJack():
        print ("\nWINNER WINNER CHICKEN DINNER!!!")
        return
    
    def DealBlackJack(Dealer):
        print ("Dealer has Blackjack. You lose\n")
        for item in Dealer:
            print ("\t" + str(item[0]))
        print ('\n')
        return
   
    def Bust1():
        print ("Your first hand busts ")
        return
    def Bust2():
        print ("Your second hand busts ")
        return

    def AceSplit():
        return

    def SplitGame(Hand, Hand2, Bank, Cards, Dealer, DealerTotal, Outcome):
        Total1 = 0
        NewTot1 = 0
        AceExp1 = 0
        Total2 = 0
        NewTot2 = 0
        AceExp2 = 0
        Outcome = ""
        Outcome1 = ""
        Outcome2 = ""
        Hand2[0] = Hand[1]
        Hand.remove(Hand[1])
        for x in range(1):
            rand = random.randint(1,52)
            while rand not in Cards:
                rand = random.randint(1,52)
            Hand2.append(Cards[rand])
            Bank.remove(Cards[rand][0])
            del Cards[rand]
        for x in range(1):
            rand = random.randint(1,52)
            while rand not in Cards:
                rand = random.randint(1,52)
            Hand.append(Cards[rand])
            Bank.remove(Cards[rand][0])
            del Cards[rand]
            
        print ("\nYour first hand contains the \n")
        
        for item in Hand:
            Total1 += int(item[1])
            print ("\t" + str(item[0]))
            if item[0][:3] == "ACE":
                AceExp1 += 1
        if AceExp1 != 0:
            if Total1 + 10 <= 21:
                NewTot1 = Total1 + 10
                print ("\nThe score of your first hand is either " + str(Total1) +
                       ' or ' + str(NewTot1) + '\n')
            elif Total1 + 10 > 21:
                NewTot1 = 0

        else:
            print ('\n')
            print ("The score of your first hand is: " + str(Total1) + '\n')


        choice1 = input("Do you (h)it or (s)tay? ")
        print ('\n')
        choice1 = choice1.lower()

        hitcount1 = 0

        while choice1 == 'h' or choice1 == 'hit':
            if Total1 <= 21:
                hitcount1 += 1
                Hit(Bank, Cards, Hand)
                Total1 += int(Hand[hitcount1+1][1])

                print ("Your first hand contains the \n")

                AceExp1 = 0

                for item in Hand:
                    if "ACE" in item[0]:
                        AceExp1 += 1
                    print ("\t" + str(item[0]))
                print ('\n')
    
                if AceExp1 != 0:
                    if Total1 + 10 <= 21:
                        NewTot1 = Total1 + 10
                        print ("Your current score is either " + str(Total1) + ' or ' + str(NewTot1))
                    else:
                        NewTot1 = 0
                        print ("Your current score is: " + str(Total1) + '\n')
                else:
                    print ("Your current score is: " + str(Total1) + '\n')
                if Total1 > 21:
                    Bust1()
                    Outcome1 = "l"
                    choice1 = 's'
            if Total1 > 21:
                Bust1()
                Outcome1 = "l"
                choice1 = 's'
            else:
                choice1 = input("Do you (h)it or (s)tay? ")
                print ('\n')
                choice1 = choice1.lower()

        print ("\nYour second hand contains the \n")

        for item in Hand2:
            Total2 += int(item[1])
            print ("\t" + str(item[0]))
            if item[0][:3] == "ACE":
                AceExp2 += 1
        if AceExp2 != 0:
            if Total2 + 10 <= 21:
                NewTot2 = Total2 + 10
                print ("\nThe score of your second hand is either " + str(Total2) +
                       ' or ' + str(NewTot2) + '\n')
            elif Total2 + 10 > 21:
                NewTot2 = 0

        else:
            print ('\n')
            print ("The score of your second hand is: " + str(Total2) + '\n')


        choice2 = input("Do you (h)it or (s)tay? ")
        print ('\n')
        choice2 = choice2.lower()

        hitcount2 = 0

        while choice2 == 'h' or choice2 == 'hit':
            if Total2 <= 21:
                hitcount2 += 1
                Hit(Bank, Cards, Hand2)
                Total2 += int(Hand2[hitcount2+1][1])

                print ("Your second hand contains the \n")

                AceExp2 = 0

                for item in Hand2:
                    if "ACE" in item[0]:
                        AceExp2 += 1
                    print ("\t" + str(item[0]))
                print ('\n')
    
                if AceExp2 != 0:
                    if Total2 + 10 <= 21:
                        NewTot2 = Total2 + 10
                        print ("Your current score is either " + str(Total2) + ' or ' + str(NewTot2))
                    else:
                        NewTot2 = 0
                        print ("Your current score is: " + str(Total2) + '\n')
                else:
                    print ("Your current score is: " + str(Total2) + '\n')
                """if Total2 > 21:
                    Bust2()
                    Outcome2 = "l"
                    choice2 = 's'"""
            if Total2 > 21:
                Bust2()
                Outcome2 = "l"
                choice2 = 's'
            else:
                choice2 = input("Do you (h)it or (s)tay? ")
                print ('\n')
                choice2 = choice2.lower()
                
        Dealercount = 0

        if Outcome1 == 'l' and Outcome2 =='l':
            LoseLose(Dealer, DealerTotal)
            Outcome = "ll"
            print ("Outcome")
            return Outcome
            

        if choice2 != 'h' or choice2 != 'hit':
            while DealerTotal < 16:
                Dealercount += 1
                Stay(Bank, Cards, Dealer)
                DealerTotal += int(Dealer[Dealercount+1][1])
            if DealerTotal > 21:
                DealBust(Dealer, DealerTotal)
                if Outcome1 != "l" and Outcome2 != "l":
                    Outcome = "ww"
                    return Outcome 
            else:
                if NewTot1 != 0:
                    if DealerTotal > NewTot1:
                        Outcome1 = "l"
                    if DealerTotal < NewTot1:
                        Outcome1 = "w"
                    if DealerTotal == NewTot1:
                        Outcome1 = "t"
                elif NewTot1 == 0:
                    if DealerTotal > Total1:
                        Outcome1 = "l"
                    elif DealerTotal < Total1:
                        Outcome1 = "w"
                    elif DealerTotal == Total1:
                        Outcome1 = "t"
                                   
                if NewTot2 != 0:
                    if DealerTotal > NewTot2:
                        Outcome2 = "l"
                    if DealerTotal < NewTot2:
                        Outcome2 = "w"
                    if DealerTotal == NewTot2:
                        Outcome2 = "t"
                elif NewTot2 == 0:
                    if DealerTotal > Total2:
                        Outcome2 = "l"
                    elif DealerTotal < Total2:
                        Outcome2 = "w"
                    elif DealerTotal == Total2:
                        Outcome2 = "t"

        Outcome = Outcome1 + Outcome2

        if Outcome == "ww":
            WinWin(Dealer, DealerTotal)
        if Outcome == "wl" or Outcome == "lw":
            WinLose(Dealer, DealerTotal)
        if Outcome == "ll":
            LoseLose(Dealer, DealerTotal)


        return Outcome



    def MainGame(Money, Bet, Outcome):
    
        Cards = {}
        Hand = []
        Hand2 = [""]
        Dealer = []
        Bank = []
        count = 0
        Total = 0
        DealerTotal = 0
        AceExp = 0
        DealAceExp = 0
        NewTot = 0
        NewDealTot = 0

        for item in Suits:
            for k,v in Values.items():
                count += 1
                Cards[count] = [str(k) + " OF " + str(item), int(v)]
                Bank.append(str(k) + " OF " + str(item))

        for x in range(2):
            rand = random.randint(1,52)
            while rand not in Cards:
                rand = random.randint(1,52)
            Hand.append(Cards[rand])
            Bank.remove(Cards[rand][0])
            del Cards[rand]

        for x in range(2):
            rand = random.randint(1,52)
            while rand not in Cards:
                rand = random.randint(1,52)
            Dealer.append(Cards[rand])
            Bank.remove(Cards[rand][0])
            del Cards[rand]

        print ("Your hand contains the \n")
        for item in Hand:
            Total += int(item[1])
            print ("\t" + str(item[0]))

            if item[0][:3] == "ACE":
                AceExp += 1                       

        if AceExp != 0:
            if Total + 10 <= 21:
                NewTot = Total + 10

                if NewTot == 21:
                    BlackJack()
                    Outcome = "b"
                    return Outcome

                print ("\nYour current score is either " + str(Total) + ' or ' + str(NewTot) + '\n')
            elif Total + 10 > 21:
                NewTot = 0

        else:
            print ('\n')
            print ("Your current score is: " + str(Total) + '\n')

        for item in Dealer:
            DealerTotal += int(item[1])

            if item[0][:3] == "ACE":
                DealAceExp += 1

        if DealAceExp != 0:
            if DealerTotal + 10 <= 21:
                NewDealTot = DealerTotal + 10
        if NewDealTot == 21:
            DealBlackJack(Dealer)
            Outcome = "l"
            return Outcome

        print ("Dealer shows: \n")
        print ("\t" + str(Dealer[0][0]))
        print ('\n')
        
        if Hand[0][0][:5] == Hand[1][0][:5] or Hand[0][1] == Hand[1][1] == 10:
            if Money - Bet > 0:
                choice1 = input("\nDo you wish to split? (Y)es or (N)o? ")
                choice1 = choice1.lower()
                if choice1 == "y":
                    #Bet2 = float(input("\nHow much do you wish to bet on your second hand? "))
                    #while Bet2 > Money - Bet:
                        #print ("You don't have that much money. Try again. ")
                        #Bet2 = float(input("\nHow much do you wish to bet on your second hand? "))
                    Outcome = SplitGame(Hand, Hand2, Bank, Cards, Dealer, DealerTotal, Outcome)
                    return Outcome
            
        choice = input("Do you (h)it or (s)tay? ")
        print ('\n')
        choice = choice.lower()

        hitcount = 0

        while choice == 'h' or choice == 'hit':
            if Total <= 21:
                hitcount += 1
                Hit(Bank, Cards, Hand)
                Total += int(Hand[hitcount+1][1])

                print ("Your hand contains the \n")

                AceExp = 0

                for item in Hand:
                    if "ACE" in item[0]:
                        AceExp += 1
                    print ("\t" + str(item[0]))
                print ('\n')

    
                if AceExp != 0:
                    if Total + 10 <= 21:
                        NewTot = Total + 10
                        print ("Your current score is either " + str(Total) + ' or ' + str(NewTot))
                    else:
                        NewTot = 0
                        print ("Your current score is: " + str(Total) + '\n')
                else:
                    print ("Your current score is: " + str(Total) + '\n')
                if Total > 21:
                    Bust()
                    Outcome = "l"
                    return Outcome
            if Total > 21:
                Bust()
                Outcome = "l"
                return Outcome
            choice = input("Do you (h)it or (s)tay? ")
            print ('\n')
            choice = choice.lower()
        Dealercount = 0
        if choice != 'h' or choice != 'hit':
            while DealerTotal < 16:
                Dealercount += 1
                Stay(Bank, Cards, Dealer)
                DealerTotal += int(Dealer[Dealercount+1][1])
            if DealerTotal > 21:
                DealBust(Dealer, DealerTotal)
                Outcome = "w"
                return Outcome
            else:
                if NewTot != 0:
                    if DealerTotal > NewTot:
                        Lose(Dealer, DealerTotal)
                        Outcome = "l"
                        return Outcome
                    if DealerTotal < NewTot:
                        Win(Dealer, DealerTotal)
                        Outcome = "w"
                        return Outcome
                    if DealerTotal == NewTot:
                        Tie(Dealer, DealerTotal)
                        Outcome = "t"
                        return Outcome
                elif NewTot == 0:
                    if DealerTotal > Total:
                        Lose(Dealer, DealerTotal)
                        Outcome = "l"
                        return Outcome
                    elif DealerTotal < Total:
                        Win(Dealer, DealerTotal)
                        Outcome = "w"
                        return Outcome
                    elif DealerTotal == Total:
                        Tie(Dealer, DealerTotal)
                        Outcome = "t"
                        return Outcome

    def Replay():
        print ("\n\nYou've lost all of your money.")
        choice = input("\nDo you wish to replay? (Y)es or (N)o?  ")
        choice = choice.lower()
        if choice == "y":
            Game()
        if choice != "y":
            return

    def Game():
        Bet2 = 0
        Money = 100
        while Money > 0:
            Outcome = ""
            print ("================================================================\n\n")
            print ("\n\nYou currently have " + str(Money))
            print ('\n')
            Bet = float(input("How much do you bet? "))
            Bet = float(Bet)
            #Bet = 1
            if Bet > Money:
                print ("You don't have that much money. Try again. ")
                Bet = float(input("\nHow much do you bet? "))
                if Bet > Money:
                    print ("You've been warned. Security will see you out now")
                    time.sleep(3.0)
                    sys.exit()
            Results = MainGame(Money, Bet, Outcome)
            #print ("Bet2 is  " + str(Bet2))

            if Results == "w":
                Money = Money + Bet
            if Results == "l":
                Money = Money - Bet
            if Results == "t":
                Money == Money
            if Results == "b":
                Money = Money + Bet*1.5
            if Results == "wl" or Results == "lw":
                Money = Money
            if Results == "ll":
                Money = Money - Bet*2
            if Results == "ww":
                Money = Money + Bet*2

            time.sleep(2.0)

        if Money == 0:
            Replay()

    Game()


GamesList = ["Blackjack"]

"""print ("Thank you for coming to the Python Casion\n")
Money = float(input("How much money do you bring with you? \n"))
print ("The current list of games we have includes: \n")
print ("\tBlackjack")
print ()
choice = input("Which game would you like to play? ")
if choice.lower() == 'blackjack':
    BlackJack(Money)"""
BlackJack()


print ("\n\n***Thank you for playing at the Python Casino***")



""" TO DO:
add bet2 for split hand
"""


    
        



