import re
"""
    re specifies a set of strings that matches it; the functions in this module let you check 
    if a particular string matches a given regular expression
"""

FIRST_NAME = "^[A-Z]{1}[a-z]{2,}$"
LAST_NAME = "^[A-Z]{1}[a-z]{2,}$"
EMAIL_ADDRESS = "^[a-zA-z]{3}[0-9a-zA-Z\\.\\_\\-\\+]*@[a-z]*\\.(co|com.au|in|net|in|com.com|com|)$"
PHONE_NUMBER = "^[0-9]{2}\s[0-9]{10}$"


class UserRegistration:
    """
    create class for validating user registration
    """

    def __init__(self):
        pass

    def first_name_validation(self, fname_input):
        """
        :return:
        :param fname_input: user input
        :return: true for valid username
        """
        if re.match(FIRST_NAME, fname_input):
            return True


    def last_name_validation(self,last_name_input):
        """
        :param last_name_input: user_input
        :return: true for valid user last name
        """
        if re.match(LAST_NAME, last_name_input):
            return True


    def email_validation(self, email_input):
        """
        :param email_input:
        :return:
        """
        if re.match(EMAIL_ADDRESS, email_input):
            return True


    def phone_number_validation(self, phone_number_input):
        """
        :param phone_number_input:
        :return:
        """
        if re.match(PHONE_NUMBER, phone_number_input):
            return True


class InputError(Exception):
    """
    Creating class for custom errors inherited from Exception class
    """
    def __init__(self, message):
        """
        :parameter message: it is inherited from Exception class
        :param message:
        """
        super().__init__(message)


if __name__ == '__main__':

    user_reg = UserRegistration()

    first_name_input = input("Enter First Name:")
    matched_input = user_reg.first_name_validation(first_name_input)
    if not matched_input:
        raise InputError(" Enter the first name with minimum three characters ")


    last_name_input = input("Enter Last Name:")
    matched_input = user_reg.last_name_validation(last_name_input)
    if not matched_input:
        raise InputError(" Enter the last name with minimum three characters ")


    emial_input = input("Enter email address:")
    matched_input = user_reg.email_validation(emial_input)
    if not matched_input:
        raise InputError("Enter the valid email")


    phone_number_input = input("Enter phone number:")
    matched_input = user_reg.phone_number_validation(phone_number_input)
    if not matched_input:
        raise InputError("Enter the valid phone number")


