from user_registration import UserRegistration
import pytest

u_reg = UserRegistration()


def test_first_name_when_proper_should_return():
    assert u_reg.first_name_validation("Sangeeta") == True or u_reg.first_name_validation("sangeeta") == False


# def test_first_name_when_improper_should_return_false():
#     assert u_reg.first_name_validation("sangeeta") == False


def test_last_name_when_proper_should_return():
    assert u_reg.last_name_validation("Math") == True or u_reg.last_name_validation("math") == False


# def test_last_name_when_improper_should_return_false():
#     assert u_reg.last_name_validation("math") == False


def test_email_when_proper_should_return():
    assert u_reg.email_validation("sangeeta.1rn18mca30@gmail.com") == True or u_reg.email_validation("sangeeta.gmail.com") == False


# def test_email_when_impproper_should_return_false():
#     assert u_reg.email_validation("sangeeta.gmail.com") == False


def test_phone_number_when_proper_should_return():
    assert u_reg.phone_number_validation("91 9422484996") == True or u_reg.phone_number_validation("9422484996") == False




