import pyperclip
import random
import pprint

print(bool("1"))
name = input()
if name:
    print("Thanks g")
else:
    print("No name")

words = ["Joon", "Lotte", "Steven"]
for i, name in enumerate(words):
    print(i+1, name)

for i in range(1, 6):
    print(f"Jimmy 5 times {i}.", sep=" rgfweroigjn")

pyperclip.copy("SKSJNAMOSIDFJ")
print(pyperclip.paste())

# Commit  vanuit visual studio code 19:07
# Inclusief commit vanuit Pycharm? 19:15


def exFunction(first_name, second_name):
    print(f"Hello {first_name}. Oh and better not forget {second_name}. The length of their names is {len(first_name)} letters and {len(second_name)} respectively.")

exFunction("Gert-Jan", "Bram")

print("12", "3", sep="separator")

# Voor verschil local vs global scope
def spam():
    eggs = 42
    print(eggs)

eggs = "Hello"
spam()
print(eggs)

# "While True" zorgt voor een oneindige loop totdat hij "break" tegenkomt. Cool voor inlogshit ofzo.
def div42by():
    while True:
        print("How many cats do you own?")
        cats = input()
        try:
            if int(cats) >  6:
                print(f"So you have {cats} cats huh. That's cool.")
            else:
                print(f"Only {cats} cats, that's nothing.")
            break
        except ValueError:
            print("Please only type numbers.")

# Gebruik van try-except, vooral handig om type van input te valideren.
def guessNum():
    print("Hi, what's your name? Let's play guess the number!")
    player_name = input()
    print(f"Well hi {player_name}, let's start!")
    correct_number = random.randint(1,10)
    guessed_number = 0
    try_number = 1

    while guessed_number != correct_number:
        try:
            print(f"Try #{try_number}. What is your guess?")
            guessed_number = int(input())
            if guessed_number != correct_number:
                if guessed_number > correct_number:
                    print("Try a lower number.")
                else:
                    print("Aim higher.")
            try_number = try_number + 1
        except ValueError:
            print("Please use numbers only.")
    print(f"Good job {player_name}, that is correct! You guessed right in {try_number} attempts.")

#guessNum()

list_example = ["een", "twee", "drie", "vier"]
print(list_example[-2]) # Negatieve index reversed de list, waar index -1 de laatste is, -2 een na laatste etc.
print(list_example[0:2]) # Slices, zelfde als R
list_example[1] = 2 # Type hoeft niet hetzelfde te zijn
print(list_example)
del list_example[1] # Verwijder item uit list
print(list_example)
print(list("Hello hi woohoo")) # Zet iedere letter in een item van een lijst
print("vijf" in list_example) # Checkt of "vijf" in lijst list_example zit, en returnt T/F
print(list_example.index("drie"))

family = ["Pap", "Mam", "Joon", "Lotte", "Steven"]
for person in range(len(family)):
    print(f"We got {family[person]}.")

name = "Steve va de Berg"
correct_name = name[:5] + "n van " + "den " + name[12:]
print(correct_name)

my_cat = {"size":"Fat", "Color":"Grey", "Disposition":"Loud"}
print(my_cat["size"])
print(my_cat.values())
print(my_cat.keys())
print(my_cat.items())

for i, j in my_cat.items():
    print(i, j)

participant = {"Name":"Steven", "Age":"24", "Gender":"Male"}
characteristics = ("Name", "Job", "Age", "Gender", "Skincolor")
print(participant)
for c in characteristics:
    if c not in participant:
        participant.setdefault(c, f"Added {c} key through for-loop.") # de get function kan iets returnen als de key ontbreekt. In tegenstelling tot setdefault, die de key toevoegt met een standaard meegegeven waarde.
print(participant)

characteristics_new = ("Length", "Weight")
for k in characteristics_new:
    print(participant.get(k, "This key does not exists.")) # de get function kan iets returnen als de key ontbreekt. In tegenstelling tot setdefault, die de key toevoegt met een standaard meegegeven waarde.


message = "Hoi ik ben steven en probeer nu te doen alsof ik dit zelf allemaal bedenk."
count = {} # Lege dictionary maken
for character in message.upper(): # Strings zijn soort van een list, dus je kan er doorheen loopen. Elke letter is 1 "list-item"
    count.setdefault(character, 0) # Checkt of de letter al bekend is. Zo niet, dan voegt hij die letter toe aan de dictionary en geeft count = 0. Deze regel is essentieel, anders heeft de dictionary niet de key voor de letter.
    count[character] += 1 # Count increment
    print(character)
pprint.pprint(count) # Module pprint maakt lange lijsten leesbaarder
