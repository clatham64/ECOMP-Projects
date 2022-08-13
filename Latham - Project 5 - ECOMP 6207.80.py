#dice game

#import functions
import random
import time
import statistics
#intialize vars
rules = 'Here are the rules:\n\
Players each get dealt 8 dice to use in up to 3 rounds. \n\
You have to win two rounds to win the game, so plan ahead! \n\
\n\
Each round:\n\
Take turns playing dice to try to get the highest total.\n\
Players can choose to "pass" and stop playing dice for the round. \n\
Passing can be a good idea because you get to keep your leftover dice for later. \n\
When one player passes, the other can keep playing dice if they want. \n\
Once both players pass, the player with the highest total gets a point (YAY!)\n\
If both players have the same total, each player gets a point. \n\
\n\
After the first round, you roll two new dice and play another round. \n\
The player that one the last round goes first. \n\
You keep your unused dice with their original values each round \n\
\n\
You keep playing rounds until one player has two point.\n\
That player wins! (Or you both tie.)\n\
Basic idea, get the highest total for two rounds. \n\
Passing lets your save your leftover dice. \n\
Remember, it doesn\'t matter how much you win by. \n\
\n'

b_hand = []
p_hand = []
p_choice = 0
first = 'bot'
f_options = ['bot','player']
p_vp = 0 #player points
b_vp = 0 #bot points
p_pass = 'no' #track if player has passed
b_pass = 'no' #track if bot has passed
b_played = 0 #played total
p_played = 0 #played total
b_p_num = 0 #number of bot dice played this round
b_check = 'no' #the bot is checking stuff
winner = 'bot'
r_num = 1 #round number

#dice rolling function
def roll(dicelist, dicenum):
    for i in range(dicenum):
        dicelist.append(random.randint(1,6))
    

#victory point function
def vpcalc(bot_dice, player_dice):
    if sum(bot_dice) > sum(player_dice):
        return('b_win')
    elif sum(bot_dice) < sum(player_dice):
        return('p_win')
    elif sum(bot_dice) == sum(player_dice):
        return('tie')

#dice selection function
def select(choice, dicelist, total):
    total = total + dicelist[choice]
    del dicelist[choice]
    return total
#welcome player and explain the rules
print('Welcome to gwenty-dice!')

print("  ____ \n\
 /\\' .\\    _____\n\
/: \\___\\  / .  /\\ \n\
\\' / . / /____/..\\ \n\
 \\/___/  \\'  '\\  / \n\
          \\'__'\\/ \n")

print(rules)
#deal each player's hand
input("Give any input when you're ready to play")

print('Great! Good luck and have fun. \n ')
time.sleep(2)
print('Rolling your dice!')
time.sleep(2)
roll(b_hand, 8)
b_hand.sort()

roll(p_hand, 8)
print('Your dice are: \n',p_hand)
print('...')
time.sleep(2)
print('Rolling the bot\'s dice...')
print('...')
time.sleep(2)

#decide who goes first
print('All set! Let\'s figure out who goes first')
first = f_options[random.randint(0,1)]
time.sleep(2)
print('Seems like the', first, 'is going first.')
time.sleep(2)

#Rounds of the game in a while loop for best 2 of 3
while p_vp < 2 and b_vp < 2:
    print('Welcome to round', r_num,'.')
    time.sleep(2)
    #start of round stuff if it's not round 1
    if r_num != 1:
        print('No one has 2 points yet, so let\'s deal 2 new dice to each player!')
        roll(p_hand, 2)
        roll(b_hand,2)
        b_hand.sort()
        print('Your hand of dice is now:', p_hand)
        time.sleep(1)
        print('Since the', first, 'won the last round (or was going first if you tied), they go first.')
        time.sleep(1)

    #loop for die selections
    while b_pass == 'no' or p_pass == 'no':
        if b_pass == 'yes':
            print('The bot has passed for the round.')
            time.sleep(2)
        if p_pass =='yes':
            print('You have passed for the round.')
            time.sleep(2)
        #Starting player offers a die if they go first
        if first == 'player' and p_pass == 'no':
            print('Your total is', p_played, 'and the bot total is', b_played, '.')
            time.sleep(1)
            going = 'yes'
            while going == 'yes':
                print('Your dice are:')
                print(p_hand)
                p_choice = input('Type the number slot of the die you want to use. \n\
(For example, press 2 for the 2nd die.) \n\
Press p to pass and stop playing for the round.')
                if p_choice.lower() == 'p':
                    print('You pass for the round. Your total is', p_played, '.')
                    p_pass = 'yes'
                    print('...')
                    time.sleep(1)
                    going = 'no'
                elif p_choice.isdigit():
                    if int(p_choice) <= len(p_hand):
                        p_choice = int(p_choice)-1
                        print('You played a', p_hand[p_choice], '.') 
                        p_played = select(p_choice, p_hand, p_played)
                        print('Your total is now:', p_played, '.')
                        going = 'no'
                        time.sleep(2)
                    elif int(p_choice)> len(p_hand):
                        print('You don\'t have that many dice. Try again.')
                        time.sleep(2)
                    else:
                        print('I don\'t understand. Try again.')
                        time.sleep(2)
                else:
                    print('I don\'t understand. Try again.')
                    time.sleep(2)
                
        #Bot turn
        if b_pass == 'no':
            #stop if the bot has no dice and tell the player how many dice the bot has
            if len(b_hand) == 0:
                print('The bot has no dice and passes with a total of', b_played)
                b_pass = 'yes'
                time.sleep(2)
                b_p_num = 0
            else:
                print('The bot has', len(b_hand),'dice left.')
                time.sleep(2)
                #Round 1 AI
                if r_num == 1:
                    if b_p_num == 0:
                        if first == 'bot':
                            print('The bot uses a', b_hand[-2], '.')
                            b_played = select(-2, b_hand, b_played)
                            print('The bot now has a total of', b_played,'.')
                            time.sleep(1)
                            b_p_num = 1
                        else:
                            if p_played > 3:
                                print('The bot uses a', b_hand[-2], '.')
                                b_played = select(-2, b_hand, b_played)
                                print('The bot now has a total of', b_played,'.')
                                time.sleep(1)
                                b_p_num = 1
                            else:
                                print('The bot uses a', b_hand[1], '.')
                                b_played = select(1, b_hand, b_played)
                                print('The bot now has a total of', b_played,'.')
                                time.sleep(1)
                                b_p_num = 1
                    else:
                        #If the bot won the round, stop
                        if b_played > p_played and p_pass == 'yes':
                            print('The bot passes with a total of', b_played)
                            b_pass = 'yes'
                            time.sleep(1)
                            b_p_num = 0
                        #If the bot is really ahead, stop
                        elif b_played > p_played + 2*statistics.mean(b_hand):
                            print('The bot passes with a total of', b_played)
                            b_pass = 'yes'
                            time.sleep(1)
                            b_p_num = 0
                        #If the player is really ahead, stop
                        elif b_played + b_hand[-1] < p_played:
                            print('The bot passes with a total of', b_played)
                            b_pass = 'yes'
                            time.sleep(1)
                            b_p_num = 0
                        #Otherwise, play high
                        else:
                            print('The bot uses a', b_hand[-1], '.')
                            b_played = select(-1, b_hand, b_played)
                            print('The bot now has a total of', b_played,'.')
                            time.sleep(1)

                #Round 2 AI
                elif r_num == 2:
                    #if the bot won the first round
                    if b_vp == 1 and p_vp == 0:
                        #If it's the first die, play something small
                        if b_p_num == 0:
                            print('The bot uses a', b_hand[0], '.')
                            b_played = select(0, b_hand, b_played)
                            print('The bot now has a total of', b_played,'.')
                            time.sleep(1)
                            b_p_num += 1
                        else:
                            #If the bot won the round, stop
                            if b_played > p_played and p_pass == 'yes':
                                print('The bot passes with a total of', b_played)
                                b_pass = 'yes'
                                time.sleep(1)
                                b_p_num = 0
                            #if the bot can win it will
                            elif b_played + sum(b_hand) > p_played and p_pass == 'yes':
                                print('The bot uses a', b_hand[0], '.')
                                b_played = select(0, b_hand, b_played)
                                print('The bot now has a total of', b_played,'.')
                                time.sleep(1) 
                            #If the bot is really ahead, stop 
                            elif p_played > b_played + 2*statistics.mean(b_hand):
                                print('The bot passes with a total of', b_played)
                                b_pass = 'yes'
                                time.sleep(1)
                                b_p_num = 0
                            #if the bot is really behind stop
                            elif b_played > p_played +2*statistics.mean(b_hand):
                                print('The bot passes with a total of', b_played)
                                b_pass = 'yes'
                                time.sleep(1)
                                b_p_num = 0
                            #if the bot is out of low dice, stop
                            elif b_hand[0] > 3:
                                print('The bot passes with a total of', b_played)
                                b_pass = 'yes'
                                time.sleep(1)
                                b_p_num = 0
                            #otherwise, play low
                            else:
                                print('The bot uses a', b_hand[0], '.')
                                b_played = select(0, b_hand, b_played)
                                print('The bot now has a total of', b_played,'.')
                                time.sleep(1)                            
                    #If the bot lost round 1 or they tied
                    else:
                        #If the bot won, stop
                        if b_played > p_played and p_pass == 'yes':
                            print('The bot passes with a total of', b_played)
                            b_pass = 'yes'
                            time.sleep(1)
                            b_p_num = 0
                        #Otherwise, play the smallest die that lets the bot be ahead
                        else:
                            i = 0 #bot checking index
                            while b_check == 'no':
                                if i == len(b_hand)-1:
                                    print('The bot uses a', b_hand[i], '.')
                                    b_played = select(i, b_hand, b_played)
                                    print('The bot now has a total of', b_played,'.')
                                    time.sleep(1)
                                    b_check = 'yes'
                                elif b_played + b_hand[i] > p_played:
                                    print('The bot uses a', b_hand[i], '.')
                                    b_played = select(i, b_hand, b_played)
                                    print('The bot now has a total of', b_played,'.')
                                    time.sleep(1)
                                    b_check = 'yes'
                                else:
                                    i = i+1
                            b_check = 'no'
                    
                #Roudn 3 AI
                #Just play dice till it's out from lowest first
                else:
                    if len(b_hand) == 0:
                        print('The bot passes with a total of', b_played)
                        b_pass = 'yes'
                        time.sleep(1)
                        b_p_num = 0
                    else:
                        print('The bot uses a', b_hand[0], '.')
                        b_played = select(0, b_hand, b_played)
                        print('The bot now has a total of', b_played,'.')
                        time.sleep(1)
                        b_check = 'yes'
                        
        #Player turn if second
        if first == 'bot' and p_pass == 'no':
            print('Your total is', p_played, 'and the bot total is', b_played, '.')
            going = 'yes'
            while going == 'yes':
                print('Your dice are:')
                print(p_hand)
                p_choice = input('Type the number slot of the die you want to use. \n\
(For example, press 2 for the 2nd die.) \n\
Press p to pass and stop playing for the round.')
                if p_choice.lower() == 'p':
                    print('You pass for the round. Your total is', p_played, '.')
                    p_pass = 'yes'
                    print('...')
                    time.sleep(1)
                    going = 'no'
                elif p_choice.isdigit():
                    if int(p_choice) <= len(p_hand):
                        p_choice = int(p_choice)-1
                        print('You played a', p_hand[p_choice], '.') 
                        p_played = select(p_choice, p_hand, p_played)
                        print('Your total is now:', p_played, '.')
                        going = 'no'
                        time.sleep(2)
                    elif int(p_choice)> len(p_hand):
                        print('You don\'t have that many dice. Try again.')
                        time.sleep(2)
                    else:
                        print('I don\'t understand. Try again.')
                        time.sleep(2)
                else:
                    print('I don\'t understand. Try again.')
                    time.sleep(2)

#Tally victory point and set first player
    print('Looks like both players have passed!')
    time.sleep(1)
    print('The bot total was', b_played, '. The player total was', p_played, '.')
    if b_played > p_played:
        print('That means the bot had a higher total and gets a point!')
        b_vp = b_vp +1
        first = 'bot'
        print('The score is bot', b_vp,'to player', p_vp, '.')
        time.sleep(3)
    elif p_played > b_played:
        print('That means the player had a higher total and gets a point!')
        p_vp = p_vp +1
        first = 'player'
        print('The score is bot', b_vp,'to player', p_vp, '.')
        time.sleep(3)
    else:
        print('That means you tied and you each get a point!')
        b_vp = b_vp + 1
        p_vp = p_vp + 1
        print('The score is bot', b_vp,'to player', p_vp, '.')
        time.sleep(3)
        
    p_played = 0
    b_played = 0
    p_pass = 'no'
    b_pass = 'no'
    r_num = r_num + 1

    
#Congradulate the winner
if b_vp == 2 and p_vp == 2:
    print('Wow, you tied! That doesn\'t happen often. Neat!')
elif b_vp == 2:
    print('Looks like the bot has 2 points and won this time around.')
else:
    print('You have 2 points and won! Congrats!')
