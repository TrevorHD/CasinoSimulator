# ----- Import packages -----------------------------------------------------------------------------------------------------

# Import packages
import random

# Define function to clear text from console
import os
def clear(): os.system('cls') #on Windows System
clear()





# ----- Pre-run setup -------------------------------------------------------------------------------------------------------

# Create a double-deck of cards
deck = list(map(str, range(2, 11, 1)))*8 + ["J", "Q", "K", "A"]*8

# Define function to shuffle double-deck
def shuffle():
    shuffleCards = random.sample(deck, len(deck))
    return shuffleCards

# Define function to check sum of any given hand
def handSum(hand):
    try:
        hSum = sum(list(map(int, hand)))
    except ValueError:
        if "A" in hand:
            h1 = ["10" if x == "J" or x == "Q" or x == "K" else x for x in hand]
            h1 = ["11" if x == "A" else x for x in h1]
            hSum = sum(list(map(int, h1)))
            while hSum > 21 and "11" in h1:
                h1[h1.index("11")] = "1"
                hSum = sum(list(map(int, h1)))
        else:
            hSum = sum(list(map(int, ["10" if x == "J" or x == "Q" or x == "K" else x for x in hand])))
    return hSum  

# Set initial values
inputError = False
cheatL = False
cheatS = False
doubled = False
split = False
dbjYes = False
dbjCheck = False
reloopD1 = False
reloopD2 = False
balance = 1000
betAmount = 0
insuranceAmount = 0
betStage = 1
dbjCheckStage = 1
dbjInsuranceStage = 0
cheatMessage = 0
decisionNumP = 1
decisionNumD = 1
turnEndTypeP = "none"
turnEndTypeD = "none"





# ----- Run game ------------------------------------------------------------------------------------------------------------

# Start running the game
while betStage >= 1:
    
    # ----- Step 1: Select Wager ----------------------------------------------
    
    # Choose amount to bet
    while betStage == 1:
        clear()
        print("-"*5, "STEP 1: Select Wager", "-"*88, "\n")
        if inputError == 1:
            print("You do not have enough credits. Please enter a smaller amount.", "\n")
        elif inputError == 2:
            print("Please enter a number greater than zero.", "\n")
        elif inputError == 3:
            print("Invalid input, try again.", "\n")
        elif cheatMessage == 1:
            print("2000 credits added to your balance. Gambling on credit seems a bit irresponsible, no?", "\n")
        elif cheatMessage == 2:
            print("1000 credits added to your balance. Who needs savings anyway?", "\n")
        elif cheatMessage == 3:
            print("You've already used this cheat code!", "\n")
        else:
            print("\n")
        print("You have", balance, "credits remaining in your account.")
        inputError = False
        cheatMessage = 0
        betAmount = input("Please enter a whole amount to wager: ")
        if betAmount == "b":
            betStage = betStage - 1
        elif betAmount in ["Loan", "loan"]:
            if cheatL == True:
                cheatMessage = 3
            else:
                balance = balance + 2000
                cheatMessage = 1
                cheatL = True
        elif betAmount in ["Savings Account", "Savings account", "savings account", "savings Account", 
                           "SavingsAccount", "Savingsaccount", "savingsaccount", "savingsAccount"]:
            if cheatS == True:
                cheatMessage = 3
            else:
                balance = balance + 1000
                cheatMessage = 2
                cheatS = True
        else:
            try:
                if int(betAmount) > balance:
                    inputError = 1
                elif int(betAmount) <= 0:
                    inputError = 2
                else:
                    betStage = betStage + 0.5
            except ValueError:
                inputError = 3
      
    # ----- Step 1.5: Initial dealing -----------------------------------------
    
    # Deal two cards to dealer and player
    while betStage == 1.5:
        cardQueue = shuffle()
        cardDealer = []
        cardPlayer = []          
        cardDealer.append(cardQueue.pop())
        cardPlayer.append(cardQueue.pop())
        cardDealer.append(cardQueue.pop())
        cardPlayer.append(cardQueue.pop())
        cardDealer = ["9", "A"]  # just for testing different scenarios
        #cardDealer = ["Q", "A"]  # just for testing different scenarios
        if handSum(cardDealer) == 21:
            dbjYes = True
        if cardDealer[1] in ["10", "J", "K", "Q", "A"]:
            dbjCheck = True
            if cardDealer[1] == "A":
                dbjInsuranceStage = 1
        betStage = betStage + 0.5
        
    # ----- Step 2: Player decisions ------------------------------------------
    
    # Allow player to take turn
    while betStage == 2:
        clear()
        print("-"*5, "STEP 2: Player Turns", "-"*88, "\n")
        if inputError == 1:
            print("Insufficient funds to double bet!", "\n")
        elif inputError == 2:
            print("Invalid input, try again.", "\n")
        elif inputError == 3:
           print("Insurance bet should be less than or equal to half of current bet, try again.", "\n")
        elif inputError == 4:
           print("Please enter a number greater than zero.", "\n")
        elif inputError == 5:
           print("Insufficient funds for desired insurance bet, try again.", "\n")
        else:
            print("\n")
        print("Dealer totals ? with cards: ?", cardDealer[1])
        print("Player totals", handSum(cardPlayer), "with cards:", *cardPlayer)
        # Can the next 7 lines be made more efficient?
        try:
            if int(insuranceAmount) > 0 and inputError not in [2, 3, 4, 5]:
                print("Your balance is", balance, "credits, with a bet of", betAmount, "plus", insuranceAmount, "in insurance.", "\n")
            else:
                print("Your balance is ", balance, " credits, with a bet of ", betAmount, ".", "\n", sep = "")
        except ValueError:
            print("Your balance is ", balance, " credits, with a bet of ", betAmount, ".", "\n", sep = "")
        if decisionNumP == 1:
            print("You were given card(s)", *cardPlayer, "\n")
        elif turnEndTypeP != "stand" and turnEndTypeP != "surrender":
            print("You were given card(s)", cardPlayer[len(cardPlayer) - 1], "\n")
        else:
            print("\n")
        inputError = False
        
        #insurance bet dialogue
        if dbjInsuranceStage == 1:
            decision = input("The dealer may possibly have blackjack. Place insurance bet? Y/N: ")
            if decision in ["N", "n", "No", "no"]:
                dbjCheckStage = 2.5
                insuranceAmount = 0
                dbjInsuranceStage = 0
            elif decision in ["Y", "y", "Yes", "yes"]:
                dbjInsuranceStage = 2
            else:
                inputError = 2
        elif dbjInsuranceStage == 2:
            insuranceAmount = input("Enter an amount less than or equal to half yout current bet: ")  
            dbjCheckStage = 1.5
            try:
                if int(insuranceAmount) > 0.5*int(betAmount):
                    inputError = 3
                elif int(insuranceAmount) <= 0:
                    inputError = 4
                elif int(insuranceAmount) > balance - int(betAmount):
                    inputError = 5
                else:
                    dbjInsuranceStage = 0
                    dbjCheckStage = 1.75
            except ValueError:
                inputError = 2
                    
        #display blackjack-checking messages
        if dbjCheck == True and dbjInsuranceStage == 0:
            if dbjCheckStage in [1, 2]:
                decision = input("The dealer checks the hole card for blackjack. Hit enter to continue... ")
                dbjCheckStage = 3
            elif dbjCheckStage in [2.5, 1.75]:
                dbjCheckStage = 2
            elif dbjCheckStage == 3:
                if int(insuranceAmount) == 0:
                    if dbjYes == False:
                        decision = input("The dealer does not have blackjack. Hit enter to continue... ")
                        dbjCheckStage = 3.5
                    elif dbjYes == True:
                        betStage = betStage + 1
                elif int(insuranceAmount) > 0:
                    if dbjYes == False:
                        decision = input("The dealer does not have blackjack, and you lose your insurance bet. Hit enter to continue... ")
                        balance = balance - int(insuranceAmount)
                        insuranceAmount = 0
                        dbjCheckStage = 3.5
                    elif dbjYes == True:
                        betStage = betStage + 1
            elif dbjCheckStage == 3.5:
                dbjCheckStage = 4
                dbjCheck = False
            
        
        if dbjCheck == False and dbjCheckStage not in [2, 3, 3.5]:
            if handSum(cardPlayer) > 21:
                if doubled == False:
                    turnEndTypeP = "bust"
                else:
                    turnEndTypeP = "doubleBust"
            elif handSum(cardPlayer) == 21 and decisionNumP == 1:
                turnEndTypeP = "blackjack"
            elif handSum(cardPlayer) <= 21 and doubled == True:
                turnEndTypeP = "doubleStand"
        
        if dbjCheck == False and dbjCheckStage not in [2, 3, 3.5]:
            if turnEndTypeP == "blackjack":
                decision = input("You have blackjack. Hit enter to continue... ")
                betStage = betStage + 1
            elif turnEndTypeP == "bust":
                decision = input("You bust; now it is the dealer's turn. Hit enter to continue... ")
                betStage = betStage + 1
            elif turnEndTypeP == "doubleBust":
                decision = input("You double down and bust; now it is the dealer's turn. Hit enter to continue... ")
                betStage = betStage + 1
            elif turnEndTypeP == "stand":
                decision = input("You stand and your turn is over; now it is the dealer's turn. Hit enter to continue... ")
                betStage = betStage + 1
            elif turnEndTypeP == "doubleStand":
                decision = input("You double down and stand; now it is the dealer's turn. Hit enter to continue... ")
                betStage = betStage + 1
            elif turnEndTypeP == "surrender":
                decision = input("You surrender and your turn is over; now it is the dealer's turn. Hit enter to continue... ")
                betAmount = int(betAmount)*0.5
                betStage = betStage + 1
            else:
                # note: will put in option for split later
                if decisionNumP == 1:
                    decision = input("Your move. Hit, stand, double down, or surrender: ")
                elif decisionNumP > 1:
                    decision = input("You're still in. Hit or stand: ")
                if decision in ["Hit", "hit"]:
                    cardPlayer.append(cardQueue.pop())
                    turnEndTypeP = "hit"
                elif decision in ["Stand", "stand"]:
                    turnEndTypeP = "stand"
                elif decision in ["Double Down", "Double down", "double down", "double Down",
                                  "Doubledown", "DoubleDown", "doubledown", "doubleDown"] and decisionNumP == 1:
                    if balance < int(betAmount)*2:
                        inputError = 1
                    else:
                        doubled = True
                        betAmount = int(betAmount)*2
                        cardPlayer.append(cardQueue.pop())
                    turnEndTypeP = "doubleDown"
                elif decision in ["Surrender", "surrender"] and decisionNumP == 1:
                    turnEndTypeP = "surrender"
                else:
                    inputError = 2
                if inputError == False:
                    decisionNumP = decisionNumP + 1
                    
        if dbjCheck == False and dbjCheckStage == 3:
            dbjCheckStage = dbjCheckStage + 1
            
    # ----- Step 3: Dealer decisions ------------------------------------------
    
    while betStage == 3:
        clear()
        print("-"*5, "STEP 3: Dealer Turns", "-"*88, "\n")
        print("\n")
        print("Dealer totals", handSum(cardDealer), "with cards:", *cardDealer)
        print("Player totals", handSum(cardPlayer), "with cards:", *cardPlayer)
        # Can the next 7 lines be made more efficient?
        try:
            if int(insuranceAmount) > 0 and inputError not in [2, 3, 4, 5]:
                print("Your balance is", balance, "credits, with a bet of", betAmount, "plus", insuranceAmount, "in insurance.", "\n")
            else:
                print("Your balance is ", balance, " credits, with a bet of ", betAmount, ".", "\n", sep = "")
        except ValueError:
            print("Your balance is ", balance, " credits, with a bet of ", betAmount, ".", "\n", sep = "")
        if decisionNumD == 1:
            print("\n")
            decision = input("Dealer reveals hole card. Press enter to continue... ")
        elif turnEndTypeD == "blackjack":
            print("\n")
            decision = input("Dealer has blackjack. Hit enter to continue... ")
            betStage = betStage + 1
        elif decisionNumD > 1 and (turnEndTypeD == "hit" or turnEndTypeD == "hitStand"):
            print("Dealer was given card(s)", cardDealer[len(cardDealer) - 1], "\n")
        else:
            print("\n")
        
        if handSum(cardDealer) == 21 and decisionNumD == 1:
            turnEndTypeD = "blackjack"
        if handSum(cardDealer) > 21:
            turnEndTypeD = "bust"
        elif handSum(cardDealer) <= 16:
            cardDealer.append(cardQueue.pop())
            turnEndTypeD = "hit"
            
        if handSum(cardDealer) in range(17, 22, 1) and turnEndTypeD != "blackjack":
            if decisionNumD > 1 and turnEndTypeD == "hit":
                turnEndTypeD = "hitStand" 
                reloopD1 = True
            elif turnEndTypeD == "hitStand" and reloopD1 == True:
                reloopD2 = True
            elif decisionNumD > 1:
                turnEndTypeD = "stand"
                
        if turnEndTypeD != "blackjack":    
            if turnEndTypeD == "bust":
                decision = input("Dealer hits and busts. Hit enter to continue... ")
                betStage = betStage + 1
            elif turnEndTypeD == "stand":
                decision = input("Dealer stands. Hit enter to continue... ")
                betStage = betStage + 1
            elif turnEndTypeD == "hitStand" and reloopD2 == True:
                decision = input("Dealer hits and then stands. Hit enter to continue... ")
                betStage = betStage + 1
            elif decisionNumD > 1 and turnEndTypeD != "hitStand":
                decision = input("Dealer hits. Press enter to continue... ")
        if inputError == False:
            decisionNumD = decisionNumD + 1
        
    # ----- Step 4: Results ---------------------------------------------------
    
    # Print appropriate result message
    while betStage == 4:
        clear()
        print("-"*5, "STEP 4: Results", "-"*93, "\n")
        if inputError == True:
            print("Invalid input, try again.", "\n")
        else:
            print("\n")
        if turnEndTypeD == "blackjack" and turnEndTypeP != "blackjack":
            if int(insuranceAmount) > 0:
                print("Dealer has blackjack; player loses, but collects insurance.")
                print("Loss of ", betAmount, ", but ", insuranceAmount, " collected from insurance.", sep = "")
                balance = balance - int(betAmount) + int(insuranceAmount)
            else:
                print("Dealer has blackjack; player loses.")
                print("Loss of ", betAmount, ".", sep = "")
                balance = balance - int(betAmount)
        if turnEndTypeD != "blackjack" and turnEndTypeP == "blackjack":
            print("Player has blackjack; dealer loses.")
            print("Payout of ", 0.5*int(betAmount), ".", sep = "")
            balance = balance + 0.5*int(betAmount)
        if turnEndTypeD == "blackjack" and turnEndTypeP == "blackjack":
            print("Push; Player and Dealer both have blackjack. Bet returned to player.")
        if turnEndTypeD != "blackjack" and turnEndTypeP != "blackjack":
            if handSum(cardDealer) > 21 and handSum(cardPlayer) > 21:
                print("Player busts with ", handSum(cardPlayer), " and dealer busts with ", handSum(cardDealer), ".", sep = "")
                print("Loss of ", betAmount, ".", sep = "")
                balance = balance - int(betAmount)
            elif handSum(cardDealer) > 21 and handSum(cardPlayer) <= 21:
                print("Player wins with ", handSum(cardPlayer), " and dealer busts with ", handSum(cardDealer), ".", sep = "")
                print("Payout of ", betAmount, ".", sep = "")
                balance = balance + int(betAmount)
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) > 21:
                print("Player busts with ", handSum(cardPlayer), " and dealer wins with ", handSum(cardDealer), ".", sep = "")
                print("Loss of ", betAmount, ".", sep = "")
                balance = balance - int(betAmount)
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) <= 21 and handSum(cardDealer) > handSum(cardPlayer):
                print("Player loses with ", handSum(cardPlayer), " and dealer wins with ", handSum(cardDealer), ".", sep = "")
                print("Loss of ", betAmount, ".", sep = "")
                balance = balance - int(betAmount)
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) <= 21 and handSum(cardDealer) < handSum(cardPlayer):
                print("Player wins with ", handSum(cardPlayer), " and dealer loses with ", handSum(cardDealer), ".", sep = "")
                print("Payout of ", betAmount, ".", sep = "")
                balance = balance + int(betAmount)
            elif handSum(cardDealer) <= 21 and handSum(cardPlayer) <= 21 and handSum(cardDealer) == handSum(cardPlayer):
                print("Push; Player and Dealer tie with ", handSum(cardPlayer), ". Bet returned to player.", sep = "")
        input("Press enter to continue... ")
        
        # Reset variables
        turnEndTypeP = "none"
        turnEndTypeD = "none"
        doubled = False
        decisionNumP = 1
        decisionNumD = 1
        reloopD1 = False
        reloopD2 = False
        betStage = 1
        dbjCheckStage = 1
        dbjCheck = False
        dbjInsuranceStage = 0
        dbjYes = False
        
        
        
        
        
    # Rules: dealer must draw on 16 and stand on 17, blackjack pays 2:1, early surrender only, double down
    #        available on soft count (even with aces) on initial hand only, blackjack pays 3:2
    