from re import match as re_match

# Alaa' Omar

numbers = []
avaliable_choices = {
    "1": "Mathematical Operations.",
    "2": "Simple Bio.",
    "3": "Exit."
}
math_operationsDict = {
    "+": "Addition.",
    "-": "Subtraction.",
    "/": "Division.",
    "*": "Multiplication.",
    "R": "Return to main menu."
}


def add(num1, num2):
    """
    Adds two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) + float(num2)


def multiply(num1, num2):
    """
    Multiplies two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) * float(num2)


def subtract(num1, num2):
    """
    Subtracts two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) - float(num2)


def divide(num1, num2):
    """
    Divides two numbers.
    Keyword arguments:
    num1-> float number,
    num2-> float number
    """
    return float(num1) / float(num2) if float(num2) else 0


def handel_input(choice):
    """" Directs the user to the suitable main menu item based """
    if (choice not in avaliable_choices):
        print("Wrong Choice! Please try again.")
        print("-" * 50)
    elif choice == "1":
        read_numbers()
        msg = " Welcome to our Main Menu:"
        print_dictionary(msg, **math_operationsDict)
        math_operation = input("Please select your operation: ")
        handel_opeartion(math_operation, numbers[0], numbers[1])

    elif choice == "2":
        name, city, familyMemberSet = enter_BioInfo()
        print_Bio(name, city, *familyMemberSet)


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


def enter_BioInfo():
    """ This functions returns user name, city and family members"""
    print("-" * 50)
    name = input("Please enter your first name: ").strip().capitalize()
    print("-" * 50)
    city = input("Please enter your city name: ").strip().capitalize()
    print("-" * 50)
    familyMemebersSet = set()
    while True:
        member = input(
            "Enter family member name, else 'e' to exit :").strip().capitalize()
        if member == 'e' or member == 'E':
            break
        else:
            familyMemebersSet.add(member)
    return name, city, familyMemebersSet


def print_Bio(name, city, *familyMembers):
    """
     This simple function prints bio information

    name -> first name (string)
    cilty ->city name (string)
    *familyMembers -> set of family members names (unpacked)

     """
    print("*" * 50)
    print(
        f"Hello Everyone,\nMy name is :'{name}', I am from '{city}' \nMy Famaily memebers are :")
    for memeber in familyMembers:
        print(f"{memeber}", end=' ,')
    print('\n')


def read_num():
    """This function reads a string number"""
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
        print("{} + {} = {}".format(num1, num2, add(num1, num2)))
    elif math_operation == "-":
        print("{} - {} = {}".format(num1, num2, subtract(num1, num2)))
    elif math_operation == "*":
        print("{} * {} = {}".format(num1, num2, multiply(num1, num2)))
    elif math_operation == "/":
        print("{} / {} = {}".format(num1, num2, divide(num1, num2)))
    else:
        print_dictionary("Welcome to the main menu", **avaliable_choices)


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
    print_dictionary(
        'Welcome to Main Menu', **avaliable_choices)
    choice = input("Please enter your choice [1, 2, 3]: ")
    if choice == "3":
        break
    handel_input(choice)
