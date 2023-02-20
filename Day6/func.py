# *** CALCULATOR ***

def calculator():
  print("**** CALCULATOR ****")
  choice_1 = int(input("Please choose first number: "))
  choice_2 = int(input("Please choose second number: "))
  choice_operator = input("Please choose operator: (+ - * /)")
  
  match choice_operator:
    case '+':
      print(add(choice_1, choice_2))
      
    case '-':
      print(subtract(choice_1, choice_2))

    case '*':
      print(multiply(choice_1, choice_2))

    case '/':
      print(divide(choice_1, choice_2))


def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def divide(num1, num2):
  return num1 / num2

calculator()