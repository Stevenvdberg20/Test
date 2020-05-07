import pyperclip
import random
import pprint
"""
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
    count.setdefault(character, 0) # Checkt of de letter(key) al bekend is. Zo niet, dan voegt hij die letter toe aan de dictionary en geeft count = 0. Deze regel is essentieel, anders heeft de dictionary niet de key voor de letter.
    count[character] += 1 # Count increment
    print(character)
pprint.pprint(count) # Module pprint maakt lange lijsten leesbaarder


################ Practice Projects ################

# Chapter 3 #

def collatz(number):
    if number % 2 == 0:
        result = number//2
    else:
        result = 3*number+1
    print(result)
    return(result)

def collatzCall():
    while True:
        try:
            collatz_num = int(input()) # Input call moet BINNEN de try clause
            temp_res = collatz(collatz_num)
            if temp_res != 1:
                print(f"{collatz_num} provided the result {temp_res}, which is not 1. Try again.")
            else:
                print(F"Using {collatz_num} the result is 1! Exiting function.")
                break
        except ValueError:
            print("Type error, try again.")

collatzCall()
"""
# Chapter 4 #

groceries = ["Apples", "Bananas", "Oranges", "Mandarins", "Garlic"]
def listToSentence(list):
    result = ""
    for i in range(len(groceries)):
        if groceries[i] != groceries[-1]:
            result = result + groceries[i] + ", "
        else:
            result = result + "and " + groceries[i] + "."
    return(result)

print(listToSentence(groceries))

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
pprint.pprint(grid[1][2]) # Lijsten volgen volgorde [row][column]

def ox():
    fin_grid = []
    for column in range(6): # Aantal columns
        grid_column = []
        for row in range(9):
            grid_column.append(grid[row][column])
        fin_grid.append(grid_column)
    return fin_grid

pprint.pprint(ox())

def createGrid(columns, rows):
    grid = []
    for row in range(rows):
        grid_row = []
        for column in range(columns):            
            grid_row.append(f"{row},{column}")
        grid.append(grid_row)
    return(grid)
pprint.pprint(createGrid(3,7))
#print(len(grid))

# Chapter 5

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
def displayInventory(dict):
    print("Inventory contains:")
    inv_total = 0
    for key in dict:
        print(f"{key} : {dict[key]}")
        inv_total += int(dict[key])
    print(f"Total number of items = {inv_total}")

displayInventory(inventory)

def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item, 1)
            print(f"Added new item to your inventory: {item}.")
        else:
            inventory[item] += 1
            print(f"Gained 1 additional {item}.")
        
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragon_loot)
displayInventory(inv)


# Chapter 6
print("Steven's \"'s morgen")
print(r"Steven's \"'s morgen") #"Raw string" (die r voor de quotes) print alle symbolen uit, en negeert python syntax binnen de string
"""
def printTable(stringList):
    col_width = [0] * len(stringList)
    for i in range(len(stringList)):
        for j in range(len(stringList[i])):
            if stringList[i][j] > col_width[i]:
                col_width[i] = stringList[i[j]]
    print(col_width)

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


printTable(tableData)
"""

## Gewoon voor mezelf, beetje kloten met dictionary en input verifieren
ex_dictionary = {"Naam":"Steven", "Leeftijd":"24", "Geslacht":"Man", "Woonplaats":"Zijderveld", "Bril":"Ja", "Diploma":"Wo"}
def randomInputTest(person_dictionary): # Functie die kijkt of de values uit de dictionary overeenkomen met de input. Beetje lelijk hardcoded, maar hij doet het wel lol
    while True:
        ex_list = list(person_dictionary.values())
        Persoon = []
        i = 0
        for item in person_dictionary.keys():
            input_field = input(f"Vermeld je {item}. \n").capitalize()
            Persoon.append(input_field)
            if input_field in person_dictionary.values():
                i = i+1
        
        if i == len(ex_list):
            print("Persoon komt overeen!")
            break
        else:
            print("Probeer opnieuw!")

#randomInputTest(ex_dictionary)

def createDictionary(len_dict):
    new_dict = {}
    for i in range(len_dict):
        k = input(f"Enter key for entry #{i+1}: ").capitalize()
        v = input(f"Enter value: for entry #{i+1}: ").capitalize()
        new_dict.setdefault(k, v)
    return new_dict

#print(createDictionary(3))


# Chapter 10 Regex
import re
messsage = "Bel me op vaste lijn in Amsterdam 020-0123456 of in Utrecht 1234567."
phone_num_regex = re.compile(r"(\d\d\d-)?(\d\d\d\d\d\d\d)") # Haakjes eromheen voor groups maken (bijvoorbeeld landcode voor telefoonnummer scheiden)
#phone_num_mo = phone_num_regex.search(messsage)
#print(phone_num_mo.group())
phone_num_mo = phone_num_regex.findall(messsage)
print(phone_num_mo[0][1]) # Van lijst op index 0, neem item op index 1
print(phone_num_mo)

#bat_regex = re.compile(r"Bat(man|woman|mobile)")
#bat_example = bat_regex.findall("Batman Batbat Batmobile")
#print(bat_example)

bat_regex1 = re.compile(r"Bat(wo)?man") # ? = het deel tussen haakjes (wo) moet 0 of 1 keer voorkomen.
bat_regex2 = re.compile(r"Bat(wo)*man") # * = 0 of meer, dus letterlijk elke mogelijkheid
bat_regex3 = re.compile(r"Bat(wo)+man") # + = 1 of meer keer voorkomen.
mo1 = bat_regex1.search("The adventures of Batwoman and Batman")
mo2 = bat_regex2.search("The adventures of Batwowowowowoman")
mo3 = bat_regex3.search("The adventures of Batman")
#print(mo3.group())

phone_regex_multiple = re.compile(r"(\d\d\d\d-)?(\d\d\d\d\d\d)+(,)?")
mo = phone_regex_multiple.findall("Nummers zijn 0123-123456, 654321 ik ben op elk nummer te bereiken.")
print(mo)

# Section 11: Files
import os
print(os.getcwd())
#os.chdir("C:\\") # Changing directory
print(os.path.abspath("Python Docs tutorial.py"))
print(os.path.relpath("C:\\Users\\steve\\Documents\\GitHub\\Test\\Udemy Automate.py", "C:\\Users\\steve")) # Controleert alleen paden TERUG, niet dieper
print(os.path.dirname("C:\\Users\\steve\\Documents\\GitHub\\Test\\Udemy Automate.py")) # Print hele pad behalve bestandnaam
print(os.path.basename("C:\\Users\\steve\\Documents\\GitHub\\Test\\Udemy Automate.py")) # Print bestandnaam
#os.makedirs("") # Kan een nieuwe map aanmaken