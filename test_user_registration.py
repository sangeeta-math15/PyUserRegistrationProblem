from user_registration import UserRegistration
import pytest

u_reg = UserRegistration()


def test_first_name_when_proper_should_return_happy():
    assert u_reg.first_name_validation("Sangeeta") == "Happy"


def test_first_name_when_proper_should_return_sad():
    assert u_reg.first_name_validation("sangeeta") == "Sad"


def test_last_name_when_proper_should_return_happy():
    assert u_reg.last_name_validation("Math") == "Happy"


def test_last_name_when_proper_should_return_sad():
    assert u_reg.last_name_validation("math") == "Sad"


def test_email_when_proper_should_return_happy():
    assert u_reg.email_validation("sangeeta.1rn18mca30@gmail.com") == "Happy"


def test_email_when_proper_should_return_sad():
    assert u_reg.email_validation("sangeeta.gmail.com") == "Sad"
