from re import match as re_match
import myMath

# Alaa' Omar

numbers = []
math_operationsDict = {
    "+": "Addition.",
    "-": "Subtraction.",
    "/": "Division.",
    "*": "Multiplication."
}


def handel_input():
    """" Directs the user to the suitable main menu item based """
    read_numbers()
    msg = " Welcome to our Main Menu:"
    print_dictionary(msg, **math_operationsDict)
    math_operation = input("Please select your operation: ")
    handel_opeartion(math_operation, numbers[0], numbers[1])


def read_numbers():
    numbers.clear()
    num1 = read_num()
    num2 = read_num()
    is_number = is_number_regex(num1) and is_number_regex(num2)
    if not is_number:
        print("One of the input values is not a number, please try again")
        read_numbers()
    else:
        numbers.append(num1)
        numbers.append(num2)


def read_num():
    """This function reads a string number"""
    print("-" * 50)
    num = input("Please enter a number: ").strip()
    print("-" * 50)
    return num


def handel_opeartion(math_operation, num1, num2):
    """ 
     This function does arethmatic operation.
     math_opeartion -> [+, -, *, /], R for main menu return
     num1= first number
     num2= second number 
     """
    if (math_operation not in math_operationsDict):
        print("-" * 50)
        print("Wrong Choice! Please try again.")
        print("-" * 50)
    elif math_operation == "+":
        print("{} + {} = {}".format(num1, num2, myMath.add(num1, num2)))
    elif math_operation == "-":
        print("{} - {} = {}".format(num1, num2, myMath.subtract(num1, num2)))
    elif math_operation == "*":
        print("{} * {} = {}".format(num1, num2, myMath.multiply(num1, num2)))
    elif math_operation == "/":
        print("{} / {} = {}".format(num1, num2, myMath.divide(num1, num2)))
    else:
        print_dictionary("Welcome to the main menu", **math_operationsDict)


def is_number_regex(s):
    """ Returns True is string is a number. """
    if re_match("^\d+?\.\d+?$", s) is None:
        return s.isdigit()
    return True


def print_dictionary(msg, **myDict):
    """ Prints any data of type dictionary
    msg -> any custome msg
    myDict -> any data of type dictionary
     """
    print("=" * 50)
    print(f'{msg}')
    print("=" * 50)
    for key, value in myDict.items():
        print("[{}] {}".format(key, value))
    print("=" * 50)


while True:
    handel_input()
