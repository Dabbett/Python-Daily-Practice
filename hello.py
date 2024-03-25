# below is simple python for the purposes to skill exercize  


# name = input("what is your name?").strip().title()

# print(f"Hello, {name}")


# objects =["hello", "world", "I", "enjoy", "full", "stack", "code"]
# print(*objects, sep=' ', end=".\n")

# another way:

name = input("what is your first and last name?").strip().title()

first, last = name.split(" ")

print(f"Hello, {first}")

print(f"Hello Mr/Mrs {last}, may I call you {first}?")
