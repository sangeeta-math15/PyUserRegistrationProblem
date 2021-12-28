"""
    re specifies a set of strings that matches it; the functions
    in this module let you check if a particular string matches a given regular expression
"""
import re

FIRST_NAME = "^[A-Z]{1}[a-z]{2,}$"
LAST_NAME = "^[A-Z]{1}[a-z]{2,}$"
EMAIL_ADDRESS = "^[a-zA-z]{3}[0-9a-zA-Z\\.\\_\\-\\+]*@[a-z]*\\.(co|com.au|in|net|in|com.com|com|)$"


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
            return "Happy"
        else:
            print("Invalid first name ")
            return "Sad"

    def last_name_validation(self,last_name_input):
        """

        :param last_name_input: user_input
        :return: true for valid user last name
        """
        if re.match(LAST_NAME, last_name_input):
            print("Valid last name")
            return "Happy"
        else:
            print("Invalid last name")
            return "Sad"

    def email_validation(self, email_input):
        if re.match(EMAIL_ADDRESS, email_input):
            print("Valid Email")
            return "Happy"
        else:
            print("Invalid Email ")
            return "Sad"

if __name__ == '__main__':
    user_reg = UserRegistration()

    first_name_input = input("Enter First Name:")
    user_reg.first_name_validation(first_name_input)

    last_name_input = input("Enter Last Name:")
    user_reg.last_name_validation(last_name_input)

    emial_input = input("Enter email address")
    user_reg.email_validation(emial_input)

