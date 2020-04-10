import pyperclip

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
    print(f"Jimmy 5 times {i}.")

pyperclip.copy("SKSJNAMOSIDFJ")
print(pyperclip.paste())

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