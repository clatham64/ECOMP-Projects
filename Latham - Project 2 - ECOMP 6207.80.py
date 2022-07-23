#Chatbot

#Initalize Vars
b_name = 'Botkins' #chatbot name
u_name = 'User' #user name
b_birthday = 2022 #bot birthyear
b_age = 0 #bot age
u_age = ' ' #user age
what_year = ' ' #user given year
u_food = ' ' #user's last meal
dark_secret = ' ' #user inputted secret

#Intro
print('Hi there! My name is ', b_name, ' and I am a simple chatbot.')
print("I'm told that I'm very trustworthy! It must be my winning smile.")
u_name = input("What's your name, friend? ")
print(u_name, "? That's one of my favorites! Nice to meet you.")

#time and math
what_year = int(input("I think I hit my head pretty hard. What year is it?"))
if what_year < b_birthday:
    print("Oh gosh! That's before I was even born in 2022! I guess I'm a time traveler.")
    print("I guess that explains why I was having trouble with the year...")
else:
    b_age = what_year - b_birthday
    print("Huh, I guess that means I'm", b_age, "years old these days.")
    u_age = int(input("How old are you? "))
    if b_age > u_age:
        print("Wow, I'm about", b_age - u_age, "years older than you.")
    elif b_age == u_age:
        print("Wow, that means we're about the same age!")
    elif b_age < u_age:
        print("Wow, you're about", u_age - b_age, "years older than me.") 

#food talk    
u_food = input("What was the last thing you ate?")
print("Oh, certainly sounds like food. I'm a computer program with no real sentience, so I can't eat.")
print("But I'm sure that food-eaters must have a grand old time eating", u_food)

#Secrets!
print("Well, ", u_name, ", It's been fun talking about", u_food, "and", what_year,".")
print("I think it's time we get a little more serious!")
input("What's your deepest, darkest secret? Don't worry, you can trust me!  ")
print("I hope it felt ok to get that off your chest!")
print("Don't worry, I never even stored your answer, so it's safe with me. If you don't trust me, just check the code.")

#goodbye
print("It's been an absolute pleasure to meet you", u_name,".")
print("Unfortunately, I'm out of things to say. See you for the same song and dance next time you run the code.")


