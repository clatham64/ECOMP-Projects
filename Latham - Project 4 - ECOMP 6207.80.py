import time
#initialize variables
n=0
items =['bag', 'granola bar'] #player items
player_ans = ''
environment = ['forest', 'river', 'cave']
e_num = 0 #environment tracker
location = ['start', 's_left', 's_right','center','river','cave', 'map', 'end']
l_num = 0 #location tracker
l_last = 0 #player's previous location
walked = False
w = '... Walking...' #Walking "animation"
fire='no' #set the fire off
at_pit = 'no'
player_ans2 = '' #answer variable for the firepit
firepit = [] #stuff in the firepit
kindling = 'no'
fuel = 'no'

#greet the player
print('Welcome to "Walking Simulator." I hope you are ready to simulate walking!')
#print('')
print('When prompted, you can pick a path by typing the number')
print('You have decided to go for a walk. You\'ve made it to a trailhead in the forest.')

while location[l_num] != 'end':
    #Start location
    while location[l_num] == 'start':
        l_last = 0
        player_ans = input("You find yourself at the enterance.\
        \nAll around you are Sticks and Pinecones. You see an information station.\
        \nThere are trailheads to your left and right.\
        \nDo you: (1) Look at the information station, (2) go left, or (3) go right.  ")

        #let the player take the sticks or pinecones
        if player_ans == 'sticks' or player_ans == 'Stick' or player_ans == 'Sticks':
           if 'sticks' not in items:
               print('You pick up some sticks and put them in your bag.')
               items = items + ['sticks']
           else :
                print('You already have sticks.')
        elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'Pinecone':
            if 'pinecones' not in items:
               print('You pick up some pinecones and put them in your bag.')
               items = items + ['pinecones']
            else:
                print('You already have pinecones.')
        #bag command
        elif player_ans == 'bag' or player_ans == 'Bag':
            for n in range(len(items)):
                if n == len(items) - 1:
                    print(items[n]+'.')
                else:
                    print(items[n], end = ', ')

        #Player goes to the map
        elif player_ans == '1':
            l_num = 6
            print('You walk to the information station.')
            print('... Walking...')
            time.sleep(3)
        #Player goes left
        elif player_ans =='2':
            walked = True
            l_num = 1
            print('... Walking...')
            time.sleep(3)
        #Player goes right
        elif player_ans == '3':
            walked = True
            l_num = 2
            print('... Walking...')
            time.sleep(3)
        #Player goes home
        elif player_ans == '4':
            if walked:
                print("What a nice walk!")
                print("Time to go home.")
                l_num = 7
            else:
                print("Sometimes it's better not to take a walk.")
                print("Time to go home. Goodbye!")
                
                l_num = 7
        else:
            print('...')
            time.sleep(2)
            print("I'm sorry, I didn't understand that. Let's try again.")
            time.sleep(2)
            print('...')

    #Player goes to the map
    while location[l_num] == 'map':
        last_l = 6
        #If the player already stole it.
        if ('map' in items):
            print ("There's nothing here. You stole the Map...")
            time.sleep(2)
            print ("Back to the trailhead!")
            print(w)
            l_num = 0
        #Players sees the map
        else :         
            print ('You see a quaint little Map of the loop.')
            print ('To the left a stream runs by the left side of the loop.')
            print ('To the right, there is a little picture of a cave.')
            print ('It seems like someone wrote something on the Map.')
            player_ans = input('Do you: (1) Inspect the writing, or (2) go back to the trailhead.  ')

            #Player Takes the Map
            if player_ans == 'map' or player_ans == 'Map':
                print('You steal the map and put it in your bag. Naughty!')
                items = items + ['map']
                
                print('You return to the trailhead.')
                l_num = 0
                print('... Walking...')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

            #Player inspects the map    
            elif player_ans == '1':
                print('You lean in close to look at the Map.')
                print('It says "If you want to try to pick something up, type the name of the item."')
                print('That Map might be useful later.')
                print('...')
                time.sleep(3)

            #Player goes back
            elif player_ans == '2':
                print("That's enough of that. Back to the trailhead.")
                print(w)
                time.sleep(2)
                l_num = 0
            else :
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

    #Left branch
    while location[l_num] == 's_left':
        #Coming from the start
        if location[l_last] == 'start':
            player_ans = input("You see a small stream. The path keeps going ahead of you.\
            \nDo you: (1) Follow the stream, (2) go onward, or (3) go back.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

            #Player goes along the stream
            elif player_ans == '1':
                l_last = 1
                l_num = 4
                print('You walk along the stream.')
                print('... Walking...')
                time.sleep(3)
                print('You follow the babbling brook until you get to the end.')

            #Player goes onward to the center
            elif player_ans =='2':
                print('You head onward.')
                l_last = 1
                l_num = 3
                print('... Walking...')
                time.sleep(3)
            #Player goes back to the start
            elif player_ans == '3':
                print('You head back.')
                l_last = 1
                l_num = 0
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        #Coming from the center
        elif location[l_last] == 'center':
            player_ans = input("You see a small stream. The path keeps going ahead of you.\
            \nDo you: (1) Follow the stream, (2) go onward, or (3) go back.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')


            #Player goes along the stream
            elif player_ans == '1':
                l_last = 1
                l_num = 4
                print('You walk along the stream.')
                print('... Walking...')
                time.sleep(3)
                print('You follow the babbling brook until you get to the end.')

            #Player goes onward to the start
            elif player_ans =='2':
                print('You head onward.')
                l_last = 1
                l_num = 0
                print('... Walking...')
                time.sleep(3)
            #Player goes back to the center
            elif player_ans == '3':
                print('You head back.')
                l_last = 1
                l_num = 3
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        #Coming from the stream
        elif location[l_last] == 'river':
            player_ans = input("You see the path you came from. The path keeps goes left and right.\
            \nDo you: (1) Follow the stream again, (2) go left, or (3) go right.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

            #Player goes along the stream
            elif player_ans == '1':
                l_last = 1
                l_num = 4
                print('You walk along the stream.')
                print('... Walking...')
                time.sleep(3)
                print('You follow the babbling brook until you get to the end.')

            #Player goes onward to the center
            elif player_ans =='2':
                print('You head left.')
                l_last = 1
                l_num = 3
                print('... Walking...')
                time.sleep(3)
            #Player goes back to the start
            elif player_ans == '3':
                print('You head right.')
                l_last = 1
                l_num = 0
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

    #right branch
    while location[l_num] == 's_right':
        #Coming from the start
        if location[l_last] == 'start':
            player_ans = input("You see a cave to the right. The path keeps going ahead of you.\
            \nDo you: (1) Explore the cave, (2) go onward, or (3) go back.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

            #Player goes cave
            elif player_ans == '1':
                l_last = 2
                l_num = 5
                print('You walk towards the cave.')
                print('... Walking...')
                time.sleep(3)

            #Player goes onward to the center
            elif player_ans =='2':
                print('You head onward.')
                l_last = 2
                l_num = 3
                print('... Walking...')
                time.sleep(3)
            #Player goes back to the start
            elif player_ans == '3':
                print('You head back.')
                l_last = 2
                l_num = 0
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        #Coming from the center
        elif location[l_last] == 'center':
            player_ans = input("You see a cave to the left. The path keeps going ahead of you.\
            \nDo you: (1) Explore the cave, (2) go onward, or (3) go back.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')
                    
            #Player goes cave
            elif player_ans == '1':
                l_last = 2
                l_num = 5
                print('You walk into the cave.')
                print('... Walking...')
                time.sleep(3)

            #Player goes onward to the Start
            elif player_ans =='2':
                print('You head onward.')
                l_last = 2
                l_num = 0
                print('... Walking...')
                time.sleep(3)
            #Player goes back to the center
            elif player_ans == '3':
                print('You head back.')
                l_last = 2
                l_num = 3
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        #Coming from the cave
        elif location[l_last] == 'cave':
            player_ans = input("You see the path you came from. The path keeps goes left and right.\
            \nDo you: (1) Go back into the cave, (2) go left, or (3) go right.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

            #Player goes cave
            elif player_ans == '1':
                l_last = 2
                l_num = 5
                print('You head back to the cave.')
                print('... Walking...')
                time.sleep(3)

            #Player goes to the start
            elif player_ans =='2':
                print('You head left.')
                l_last = 2
                l_num = 0
                print('... Walking...')
                time.sleep(3)
            #Player goes to the center
            elif player_ans == '3':
                print('You head right.')
                l_last = 2
                l_num = 3
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')
    #center
    while location[l_num] == 'center':
        #Coming from the left
        if location[l_last] == 's_left':
            player_ans = input("You see a beautiful boulder to the left. The path keeps going ahead of you.\
            \nDo you: (1) Meditate on the boulder, (2) go onward, or (3) go back.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

                    
            #Player goes rock
            elif player_ans == '1':
                print('You walk over to the rock and sit down to meditate.')
                time.sleep(3)
                print('...')
                time.sleep(3)
                print('......')
                time.sleep(3)
                print('This mindfulness is reminding you that you can look in your bag.\
                \nYou just have to type "bag" when you have a choice.')
                time.sleep(3)
                print('...')
                print('Well, that was nice. You head back to the path.')
                print(w)

            #Player goes onward to the right
            elif player_ans =='2':
                print('You head onward.')
                l_last = 3
                l_num = 2
                print('... Walking...')
                time.sleep(3)
            #Player goes back to the left
            elif player_ans == '3':
                print('You head back.')
                l_last = 3
                l_num = 1
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        #Coming from the right
        elif location[l_last] == 's_right':
            player_ans = input("You see a beautiful boulder to the right. The path keeps going ahead of you.\
            \nDo you: (1) Meditate on the boulder, (2) go onward, or (3) go back.  ")

            #let the player take the sticks or pinecones
            if player_ans == 'sticks' or player_ans == 'stick' or player_ans == 'Sticks':
               if 'sticks' not in items:
                   print('You pick up some sticks and put them in your bag.')
                   items = items + ['sticks']
               else :
                    print('You already have sticks.')
            elif player_ans == 'pinecones' or player_ans == 'Pinecones' or player_ans == 'pinecone':
                if 'pinecones' not in items:
                   print('You pick up some pinecones and put them in your bag.')
                   items = items + ['pinecones']
                else:
                    print('You already have pinecones.')
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')
                    
            #Player goes rock
            elif player_ans == '1':
                print('You walk over to the rock and sit down to meditate.')
                time.sleep(3)
                print('...')
                time.sleep(3)
                print('......')
                time.sleep(3)
                print('This mindfulness is reminding you that you can look in your bag.\
                \nYou just have to type "bag" when you have a choice.')
                time.sleep(3)
                print('...')
                print('Well, that was nice. You head back to the path.')
                print(w)

            #Player goes onward to the left
            elif player_ans =='2':
                print('You head onward.')
                l_last = 3
                l_num = 1
                print('... Walking...')
                time.sleep(3)
            #Player goes back to the right
            elif player_ans == '3':
                print('You head back.')
                l_last = 3
                l_num = 2
                print('... Walking...')
                time.sleep(3)
            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

    #river
    while location[l_num] == 'river':
        print("There's a lovely spring. Unfortunately, there's also a lot of litter.")
        #If they don't have the lighter yet
        if 'lighter' not in items:
            player_ans = input("You see an endless suply of Beer Cans and a Lighter.\
            \nDo you: (1) Solemnly observe, or (2) go back.  ")

            #let the player take the trash
            if player_ans == 'Can' or player_ans == 'Beer' or player_ans == 'Beer Can' or player_ans == 'Beer Cans' or player_ans == 'beer cans':
                print('You pick up a beer can and put it in your bag.')
                print("There are still so many left...")
                items = items + ['beer can']
                time.sleep(2)
            elif player_ans == 'lighter' or player_ans == 'Lighter':
                print('You pick up the ligher and put it in your bag.')
                print('Might come in handy.')
                time.sleep(2)
                items = items + ['lighter']
            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

                    
            #Player is solemn
            elif player_ans == '1':
                print('...')
                time.sleep(3)
                print('What a mess.')
                time.sleep(3)
                print('...')
                time.sleep(3)

            #Player goes back
            elif player_ans =='2':
                print('You head back.')
                l_last = 4
                l_num = 1
                print('... Walking...')
                time.sleep(3)

            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        else:
            player_ans = input("You see an endless suply of beer cans.\
            \nDo you: (1) Solemnly observe, or (2) go back.  ")

            #let the player take the trash
            if player_ans == 'can' or player_ans == 'beer' or player_ans == 'beer can' or player_ans == 'beer cans':
                print('You pick up a beer can and put it in your bag.')
                print("There are still so many left...")
                items = items + ['beer can']
                time.sleep(2)
            elif player_ans == 'lighter' or player_ans == 'Lighter':
                print('You already took that.')
                time.sleep(2)

            #bag command
            elif player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')
                   
            #Player is solemn
            elif player_ans == '1':
                print('...')
                time.sleep(3)
                print('What a mess.')
                time.sleep(3)
                print('...')
                time.sleep(3)

            #Player goes back
            elif player_ans =='2':
                print('You head back.')
                l_last = 4
                l_num = 1
                print('... Walking...')
                time.sleep(3)

            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

    #cave
    while location[l_num] == 'cave':
        print("You walk into the cave.")
        if fire == 'no':
            print("It's a bit dark. There's a firepit in the cave." )
            player_ans = input("Do you: (1) head over to the firepit, or (2) head back to the path.  ")
            #bag Check
            if player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

                    
            #Player goes to the firepit
            elif player_ans == '1':
                at_pit = 'yes'
                #if it's empty
                while at_pit == 'yes':
                    if fire == 'no':
                        if firepit == []:
                            print("It's an empty firepit." )
                        elif firepit != [] and fire == 'no':
                            print("The fire pit has ", firepit, "in it.")
                        player_ans2 = input("Do you: (1) put something in it, (2) try to light a fire, or (3) step away.  ")
                        #bag Check
                        if player_ans2 == 'bag' or player_ans == 'Bag':
                            for n in range(len(items)):
                                if n == len(items) - 1:
                                    print(items[n]+'.')
                                else:
                                    print(items[n], end = ', ')
                        elif player_ans2 == '1':
                            pit_check = input('What do you put in the firepit? ')
                            if pit_check in items and (pit_check == 'pinecones' or pit_check == 'map'):
                                if kindling == 'no':
                                    print('Good idea! The ', pit_check, ' should make good kindling.')
                                    items.remove(pit_check)
                                    firepit = firepit + [pit_check]
                                    kindling = 'yes'
                                    time.sleep(3)
                                elif kindling == 'yes':
                                    print('You should already have enough kindling.')
                                    time.sleep(3)
                            elif pit_check in items and (pit_check == 'sticks' or pit_check == 'granola bar'):
                                if fuel == 'no':
                                    print('Good idea! The ', pit_check, ' should make good fuel for the fire.')
                                    items.remove(pit_check)
                                    firepit = firepit + [pit_check]
                                    fuel = 'yes'
                                    time.sleep(3)
                                elif fuel == 'yes':
                                    print('You should already have enough fuel for the fire.')
                                    time.sleep(3)
                            elif pit_check in items:
                                print("That doesn't seem like it would help.")
                                time.sleep(2)
                            elif pit_check not in items:
                                print("You don't have ", pit_check," in your bag. (Careful, case sensitive)")
                                time.sleep(2)
                            else:
                                print('...')
                                time.sleep(2)
                                print("I'm sorry, I didn't understand that. Let's try again.")
                                time.sleep(2)
                                print('...')    
                        elif player_ans2 == '2':
                            if kindling == 'yes' and fuel == 'yes' and 'lighter' in items:
                                print('You use the lighter to light the kindling.')
                                print('The fuel catches and you have a cozy fire!')
                                fire = 'on'
                                time.sleep(2)
                            elif kindling == 'no' and fuel == 'yes':
                                print('You have fuel but no kindling.')
                                time.sleep(2)
                            elif kindling == 'yes' and fuel == 'yes' and 'lighter' not in items:
                                print('You have fuel for the fire and kindling, but no way to light it.')
                                time.sleep(2)
                            elif kindling == 'yes' and fuel == 'no':
                                print('You have kindling but no fuel for the fire.')
                                time.sleep(2)
                            elif kindling == 'no' and fuel == 'no':
                                print('You have no fuel for the fire, nor any kindling.')
                            else:
                                print('Something is wrong. Not sure what.')
                        elif player_ans2 == '3':
                            print('You back away from the firepit')
                            time.sleep(2)
                            print('...')
                            at_pit = 'no'
                        else:
                            print('...')
                            time.sleep(2)
                            print("I'm sorry, I didn't understand that. Let's try again.")
                            time.sleep(2)
                            print('...')
                    elif fire == 'on':
                        print("There is a warm fire casting its glow.")
                        player_ans2 = input("Do you: (1) sit by the fire, or (2) step away.  ")
                        #Pit sit
                        if player_ans2 == '1':
                            print('Feels nice.')
                            time.sleep(3)
                        #leave pit
                        elif player_ans2 == '2':
                            print('You back away from the firepit')
                            time.sleep(2)
                            print('...')
                            at_pit = 'no'
                        elif player_ans2 == 'bag':
                            for n in range(len(items)):
                                if n == len(items) - 1:
                                    print(items[n]+'.')
                                else:
                                    print(items[n], end = ', ')
                        else:
                            print('...')
                            time.sleep(2)
                            print("I'm sorry, I didn't understand that. Let's try again.")
                            time.sleep(2)
                            print('...')     
                

            #Player goes back
            elif player_ans =='2':
                print('You head back.')
                l_last = 5
                l_num = 2
                print('... Walking...')
                time.sleep(3)

            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        elif fire == 'on':
            print("It's nice and bright in here because of the fire. You can now see some writing on the wall." )
            player_ans = input("Do you: (1) head over to the firepit, (2) head back to the path, or (3) read the writing.  ")
            #bag Check
            if player_ans == 'bag' or player_ans == 'Bag':
                for n in range(len(items)):
                    if n == len(items) - 1:
                        print(items[n]+'.')
                    else:
                        print(items[n], end = ', ')

                    
            #Player goes to the firepit
            elif player_ans == '1':
                at_pit = 'yes'
                #if it's empty
                while at_pit == 'yes':
                    print("There is a warm fire casting its glow.")
                    player_ans2 = input("Do you: (1) sit by the fire, or (2) step away.  ")
                    #Pit sit
                                #bag Check
                    if player_ans2 == 'bag' or player_ans == 'Bag':
                        for n in range(len(items)):
                            if n == len(items) - 1:
                                print(items[n]+'.')
                            else:
                                print(items[n], end = ', ')
                    elif player_ans2 == '1':
                        print('Feels nice.')
                        time.sleep(3)
                    #leave pit
                    elif player_ans2 == '2':
                        print('You back away from the firepit')
                        time.sleep(2)
                        print('...')
                        at_pit = 'no'
                    else:
                        print('...')
                        time.sleep(2)
                        print("I'm sorry, I didn't understand that. Let's try again.")
                        time.sleep(2)
                        print('...')     
                

            #Player goes back
            elif player_ans =='2':
                print('You head back.')
                l_last = 5
                l_num = 2
                print('... Walking...')
                time.sleep(3)
            #player reads cave
            elif player_ans =='3':
                print('It says, "If you press (4) at the trailhead you can go home."')
                time.sleep(3)
                print('...')

            else:
                print('...')
                time.sleep(2)
                print("I'm sorry, I didn't understand that. Let's try again.")
                time.sleep(2)
                print('...')

        

