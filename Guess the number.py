import random


# function generates a random number between 0 and 100
def generate_number():
    number = random.randrange(0, 100)
    return number


# main function to let the user guess the generated number
def guess_the_number():
    while True:
        g = input("Bitte gib eine Zahl zwischen 0 und 100 eingeben. ")
        try:
            guess = int(g)
            if guess > number:
                a1 = random.choice(["Es tut mir leid, leider ist die von dir eingegebene Zahl zu hoch.",
                                    "Tut mir leid " + name + ", leider zu hoch.",
                                    name + ", die Zahl ist leider zu hoch.",
                                    "Leider ist die von dir eingegebene Zahl zu hoch."])
                print(a1)
            if guess < number:
                a2 = random.choice(["Es tut mir leid, leider ist die von dir eingegebene Zahl zu niedrig.",
                                    "Schade " + name + ", leider zu niedrig.",
                                    name + " ,leider ist deine Zahl zu niedrig.",
                                    "Die von dir eingegebene Zahl ist leider zu niedrig."])
                print(a2)
            if guess == number:
                print("Herzlichen Glückwunsch " + name + " ,du hast die richtige Zahl erraten!! " + str(number))
                new_round()
                exit()
        except ValueError:
            print("Bitte nur Zahlen von 0 bis 100 verwenden.")


# function asks for a retry
def new_round():
    while True:
        answer = input(" Möchtest du es noch einmal versuchen? Ja oder Nein ")
        if answer in ["ja", "j", "Ja", "J"]:
            print("Okay " + name + ", neue Runde")
            guess_the_number()
        if answer in ["Nein", "nein", "ne", "Ne"]:
            print("Auf wiedersehen " + name + ", bis zum nächsten mal")
            exit()
        else:
            print("Bitte mit ja oder nein antworten")


if __name__ == '__main__':
    name = input("Hallo, magst du mir deinen Namen verraten? ")
    print("Guten Tag " + name + ". Lass uns anfangen!")
    number = generate_number()
    guess_the_number()
