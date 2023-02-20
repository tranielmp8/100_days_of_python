# FAMOUS FIZZBUZZ Questions

for number in range(0, 101):
  if number % 5 == 0 and number % 3 == 0:
    print("FizzBuzz!")
  elif number % 3 == 0:
    print("Fizz!")
  elif number % 5 == 0:
    print("Buzz!")
  else:
    print(number)