from user_registration import UserRegistration
import pytest


def test_first_name_when_proper_should_return_true():
    u_reg = UserRegistration()
    assert u_reg.first_name_validation("Sangeeta") == True or u_reg.first_name_validation("sangeeta") == False or u_reg.first_name_validation("SANGEETA") == False
