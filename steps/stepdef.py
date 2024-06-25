
from behave import *

from utilities import common_methods


@given(u'User is preparing to test {keyword_var}')
def step1(self, keyword_var):
    print('test_step_1')
    print("keyword = " + keyword_var)
    common_methods.hard_assert("a", "a")

@when(u'test_step_2')
def step2(self):
    print('test_step_2')

@then(u'test_step_3')
def step3(self):
    print('test_step_3')