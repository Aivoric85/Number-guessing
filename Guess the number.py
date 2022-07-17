import random


def mainmenue_de():
    name = input("Magst du mir deinen Namen verraten? \n")
    print("Guten Tag " + name + ". Lass uns anfangen!")
    guess_the_number_de(name)


# main function to generate a random number the user has to guess in german
def guess_the_number_de(name):
    print("Ich überlege mir eine Zahl zwischen 0 und 100 und du musst raten welche es ist!")
    number = random.randrange(0, 100)
    while True:
        g = input("Bitte gib eine Zahl zwischen 0 und 100 eingeben. \n")
        try:
            guess = int(g)
            if guess > number:
                print(random.choice(["Leider ist die von dir eingegebene Zahl zu hoch. Versuche es noch einmal.",
                                     "Tut mir leid " + name + ", leider zu hoch. Versuche es noch einmal.",
                                     name + ", die Zahl ist leider zu hoch. Versuche es noch einmal.",
                                     "Leider ist die von dir eingegebene Zahl zu hoch. Versuche es noch einmal."]))
            if guess < number:
                print(random.choice(["Leider ist die von dir eingegebene Zahl zu niedrig. Versuche es noch einmal.",
                                     "Schade " + name + ", leider zu niedrig. Versuche es noch einmal.",
                                     name + ", leider ist deine Zahl zu niedrig. Versuche es noch einmal.",
                                     "Die von dir eingegebene Zahl ist leider zu niedrig. Versuche es noch einmal."]))
            if guess == number:
                print("Herzlichen Glückwunsch " + name + ", du hast die richtige Zahl erraten!! " + str(number))
                new_round_de(name)
        except ValueError:
            print("Bitte nur Zahlen von 0 bis 100 verwenden.")


# function asks for a retry
def new_round_de(name):
    while True:
        answer = input("Möchtest du es noch einmal versuchen? Tippe ja oder nein \n")
        if answer in ["ja", "j", "Ja", "J"]:
            print("Okay " + name + ", neue Runde")
            guess_the_number_de(name)
        if answer in ["Nein", "nein", "ne", "Ne", "N", "n"]:
            print("Auf Wiedersehen " + name + ", bis zum nächsten mal")
            exit()
        else:
            print("Bitte mit ja oder nein antworten")


def mainmenue_en():
    name = input("Hi, would yo tell me your name?\n")
    print("Hello " + name + ". Let's get started!")
    guess_the_number_en(name)


# main function to generate a random number the user has to guess in english
def guess_the_number_en(name):
    print("I got a number between 0 and 100 in mind. Can you guess witch?")
    number = random.randrange(0, 100)
    while True:
        g = input("Please enter a number between 0 and 100. \n")
        try:
            guess = int(g)
            if guess > number:
                print(random.choice(["Sorry, the number you have entered is to high. Please try again.",
                                     "Sorry " + name + ", to high. Please try again.",
                                     name + ", the number you picked is to high. Please try again.",
                                     "The number you have chosen is to high. Please try again."]))
            if guess < number:
                print(random.choice(["Sorry, the number you have entered is to low. Please try again.",
                                     "Sorry " + name + ", to low. Please try again.",
                                     name + ", the number you picked is to low. Please try again.",
                                     "The number you entered is to low... Sorry. Please try again."]))
            if guess == number:
                print("Congratulations " + name + "!! You got the correct number. " + str(number))
                new_round_en(name)
        except ValueError:
            print("Please only use numbers between 0 and 100.")


# function asks for a retry
def new_round_en(name):
    while True:
        answer = input("Would you like to try again? Type yes or no. \n")
        if answer in ["yes", "y"]:
            print("Okay " + name + ". One more try!")
            guess_the_number_en(name)
        if answer in ["no", "n"]:
            print("Good bye " + name + ". See you next time.")
            exit()
        else:
            print("Please use yes/y or no/n")


while True:
    lang = input("Hello, please choose an Language. \nFür deutsche tippe bitte: de \nFor english please type: en \n")
    if lang == "de":
        mainmenue_de()
    if lang == "en":
        mainmenue_en()
    else:
        print("Ops, " + str(lang) + " is no valid option.")
