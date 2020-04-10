a, b = 0, 1
while a < 1000:
    print(f"The value of \"a\" equals {a}.")
    a, b = b, a + b

words = ["Steven", "Joon", "Lotte"]

i = 1
for name in words:
    print(f"{name} is person {i} in Words.")
    i = i + 1

# Enumerate creates numbered tuples, convenient for lists/dictionaries
for v in enumerate(words, start=1):
    print(v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print(f"What is your {q}?  It is {a}.")


# Nieuwe branch aangemaakt, kijken of committen nu wel lukt
# Commit  vanuit visual studio code 19:07
# Inclusief commit vanuit Pycharm? 19:15

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            print("y, ye, or yes registered.")
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            print("n, no, nop, or nope registered.")
            return False
        retries = retries - 1
        if retries < 0:
            print("No tries left, loop exited.")
            raise ValueError('invalid user response')
        print(reminder)