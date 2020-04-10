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