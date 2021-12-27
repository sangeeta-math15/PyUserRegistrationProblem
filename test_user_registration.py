from user_registration import UserRegistration
import pytest

def test_first_name():
    u_reg = UserRegistration()
    assert u_reg.first_name_validation("Sangeeta") == True or u_reg.first_name_validation("sangeeta") == False or u_reg.first_name_validation("SANGEETA") == False




