from user_registration import UserRegistration
import pytest

u_reg = UserRegistration()


def test_first_name_when_proper_should_return_true():
    assert u_reg.first_name_validation("Sangeeta") == True or u_reg.first_name_validation("sangeeta") == False or u_reg.first_name_validation("SANGEETA") == False


def test_last_name_when_proper_should_return_true():
    assert u_reg.last_name_validation("Math") == True or u_reg.last_name_validation("math") == False or u_reg.last_name_validation("MATH")
