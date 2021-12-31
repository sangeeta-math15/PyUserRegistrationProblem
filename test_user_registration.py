from user_registration import UserRegistration

import pytest

u_reg = UserRegistration()


def test_first_name():
    """
    :return: true for valid first name otherwise false
    """
    assert u_reg.first_name_validation("Sangeeta") == True or u_reg.first_name_validation("sangeeta") == False


def test_last_name():
    """
    :return: true for valid last name otherwise false
    """
    assert u_reg.last_name_validation("Math") == True or u_reg.last_name_validation("math") == False


def test_email():
    """
    :return: true for email validation otherwise false
    """
    assert u_reg.email_validation("sangeeta.1rn18mca30@gmail.com") == True or u_reg.email_validation("sangeeta.gmail.com") == False


def test_phone_number():
    """
    :return: true for phone number validation otherwise false
    """
    assert u_reg.phone_number_validation("91 9422484996") == True or u_reg.phone_number_validation("9422484996") == False


def test_password():
    """
    :return: true for password validation correct otherwise false
    """
    assert u_reg.password_validation("Sang@1234") == True or u_reg.password_validation("sang@math") == False
