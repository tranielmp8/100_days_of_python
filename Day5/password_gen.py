import random
from characters import letters, numbers, symbols

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []
super_pass=""

for _ in range(0 , nr_letters):
  password.append(random.choice(letters))
for _ in range(0 , nr_symbols):
  password.append(random.choice(symbols))
for _ in range(0 , nr_numbers):
  password.append(random.choice(numbers))

print(password)
random.shuffle(password)
for char in password:
  super_pass += char

print(f"your super password is: {super_pass}")
