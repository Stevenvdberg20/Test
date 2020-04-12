import pyperclip
import random

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

guessNum()