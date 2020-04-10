:import pyperclip

print(bool(""))
name = input()
if name:
    print("Thanks g")
else:
    print("No name")

words = ["Joon", "Lotte", "Steven"]
for i, name in enumerate(words):
    print(i+1, name)

for i in range(1, 6):
    print(f"Jimmy 5 times {i}.")

pyperclip.copy("SKSJNAMOSIDFJ")
print(pyperclip.paste())

# Commit  vanuit visual studio code 19:07