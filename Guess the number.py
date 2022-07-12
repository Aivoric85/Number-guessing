import random


# main function to generate a random number the user has to guess
def guess_the_number():
    number = random.randrange(0, 100)
    while True:
        g = input("Bitte gib eine Zahl zwischen 0 und 100 eingeben. ")
        try:
            guess = int(g)
            if guess > number:
                a1 = random.choice(["Leider ist die von dir eingegebene Zahl zu hoch. Versuche es noch einmal",
                                    "Tut mir leid " + name + ", leider zu hoch. Versuche es noch einmal",
                                    name + ", die Zahl ist leider zu hoch. Versuche es noch einmal",
                                    "Leider ist die von dir eingegebene Zahl zu hoch.Versuche es noch einmal"])
                print(a1)
            if guess < number:
                a2 = random.choice(["Leider ist die von dir eingegebene Zahl zu niedrig.Versuche es noch einmal",
                                    "Schade " + name + ", leider zu niedrig. Versuche es noch einmal",
                                    name + ", leider ist deine Zahl zu niedrig. Versuche es noch einmal",
                                    "Die von dir eingegebene Zahl ist leider zu niedrig. Versuche es noch einmal"])
                print(a2)
            if guess == number:
                print("Herzlichen Glückwunsch " + name + ", du hast die richtige Zahl erraten!! " + str(number))
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
        if answer in ["Nein", "nein", "ne", "Ne", "N", "n"]:
            print("Auf wiedersehen " + name + ", bis zum nächsten mal")
            exit()
        else:
            print("Bitte mit ja oder nein antworten")


if __name__ == '__main__':
    print("Hallo, lass uns ein Spiel spielen. Ich überlege mir eine Zahl und du musst raten welche es ist!")
    name = input("Magst du mir deinen Namen verraten? ")
    print("Guten Tag " + name + ". Lass uns anfangen!")
    guess_the_number()
