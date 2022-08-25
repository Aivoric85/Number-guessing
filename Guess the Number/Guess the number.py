import random, gettext, json


# main function guess a random number
def guess_the_number(name, number, attempt):
    print(_("Please enter a number between 0 and 100."))
    while True:
        try:
            guess = int(input())
            check_number(name, guess, number, attempt)
        except ValueError:
            print(_("Please only use numbers between 0 and 100."))


# Compare's generatted number and user input
def check_number(name, guess, number, attempt):
    attempt = attempt + 1
    if guess > number:
        print(random.choice([_("Sorry, the number you have entered is to high. Please try again."),
                             _("Sorry %s, to high. Please try again.") % (name),
                             _("%s, the number you picked is to high. Please try again.") % (name),
                             _("The number you have chosen is to high. Please try again.")]))
        guess_the_number(name, number, attempt)
    if guess < number:
        print(random.choice([_("Sorry, the number you have entered is to low. Please try again."),
                             _("Sorry %s, to low. Please try again.") % (name),
                             _("%s, the number you picked is to low. Please try again.") % (name),
                             _("The number you entered is to low... Sorry. Please try again.")]))
        guess_the_number(name, number, attempt)
    if guess == number:
        print(_("Congratulations %s!! You got the correct number %s. You have tryed %s times.") % (name, number, attempt))
        save_score(name, attempt)
        retry(name)
                

# Ask's for a retry
def retry(name):
    answer = input(_("Would you like to try again? Type yes or no. \n"))
    if answer in [_("yes"), _("y")]:
        print(_("Okay %s. One more try!") % (name))
        generate_number(name)
    if answer in [_("no"), _("n")]:
        print(_("Good bye %s. See you next time.") % (name))
        exit()
    else:
        print(_("Please use yes/y or no/n"))

# Generates a random Number
def generate_number(name):
    number = random.randrange(0, 100)
    guess_the_number(name, number, attempt)


def set_language():
    while True:
        print("Hello, let us choose a Language: \nFor englisch typ: en \nFür deutsch tippe: de ")
        lang = input()
        if lang == "en":
            t = gettext.translation('Guess_en', localedir='Lang', languages=['en'])
            _ = t.gettext
            return _
        elif lang == "de":
            t = gettext.translation('Guess_de', localedir='Lang', languages=['de'])
            _ = t.gettext
            return _ 
        else:
            print("Sorry %s, is no valid option." % (lang))


def save_score(name, attempt):
    user = {'Name' : name, 'Attempts' : attempt}
    json.dump(user , open('Guess the Number\GtN_score.json', 'w'), indent= 4, separators= (',' ,': '))


attempt = 0
name = 'Player'
_ = set_language()
name = input(_("Hi, would you tell me your name?\n"))
print(_("Hello %s. Let's get started!") % (name))
print(_("I got a number between 0 and 100 in mind. Can you guess wich?"))
generate_number(name)
