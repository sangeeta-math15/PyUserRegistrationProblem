"""
    re specifies a set of strings that matches it; the functions
    in this module let you check if a particular string matches a given regular expression
"""
import re

FIRST_NAME = "^[A-Z]{1}[a-z]{2,}$"


class UserRegistration:

    def __init__(self):
        pass

    def first_name_validation(self, fname_input):
        """
        :return:
        :param fname_input: user input
        :return: true for valid username
        """
        if re.match(FIRST_NAME, fname_input):
            print("Valid first name")
            return True
        else:
            print("Invalid first name ")
            return False


if __name__ == '__main__':
    user_reg = UserRegistration()
    first_name_input = input("Enter First Name:")
    user_reg.first_name_validation(first_name_input)
