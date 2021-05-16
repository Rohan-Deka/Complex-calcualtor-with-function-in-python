
from art import logo

def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/" : divide,
}
def calculator():
    print(logo)
    num1 = float(input("What is the first number: ")) 

    for operator in operations:
        print(operator)

    should_continue = True
    while should_continue:

        symbol = input("Pick an operation : ")

        num2 = float(input("What is the next number: "))

        calculation= operations[symbol]
        answer = calculation(num1,num2)

        print(f"{num1} {symbol} {num2} = {answer}")

        if input(f"Type 'y' continue with the {answer} of type 'n' to start a new calculation ") == 'y':
            num1 = answer

        else:
            should_continue = False
            calculator()

calculator()
