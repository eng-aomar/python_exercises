import sphere
from re import match as re_match


# Alaa' Omar
r = []


def is_number_regex(s):
    """ Returns True is string is a number. """
    if re_match("^\d+?\.\d+?$", s) is None:
        return s.isdigit()
    return True


def read_number():
    r.clear()
    num1 = read_num()
    is_number = is_number_regex(num1)
    if not is_number:
        print("One of the input values is not a number, please try again")
        read_numbers()
    else:
        r.append(float(num1))


def read_num():
    """This function reads a string number"""
    print("-" * 50)
    num = input("Please enter a number: ").strip()
    print("-" * 50)
    return num


while True:
    read_number()
    vplume = sphere.getVolume(r[0])
    print(f'The sphere volume with radius {r} is {vplume:,f}')
