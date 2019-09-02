# Practice: Sensitive Information
# Create a class to represent a patient of a doctor's office. The Patient class will accept the following information during initialization

# Social security number
# Date of birth
# Health insurance account number
# First name
# Last name
# Address
# The first three properties should be read-only. First name and last name should not be exposed as properties at all, but instead expose a calculated property of full_name. Address should have a getter and setter.

# cashew = Patient(
#     "097-23-1003", "08/13/92", "7001294103",
#     "Daniela", "Agnoletti", "500 Infinity Way"
# )

# # This should not change the state of the object
# cashew.social_security_number = "838-31-2256"

# # Neither should this
# cashew.date_of_birth = "01-30-90"

# # But printing either of them should work
# print(cashew.social_security_number)   # "097-23-1003"

# # These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# # But this should output the full name
# print(cashew.full_name)   # "Daniela Agnoletti"


class Patient:

    def __init__(self, ss_number, date_of_birth, hinsacct_number, first_name, last_name, address):
        self.__ss_number = ss_number
        self.__date_of_birth = date_of_birth
        self.__health_insurance_account_number = hinsacct_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.address = address

    # read only on first 3 properties--ss#, birthdate, hins#
    @property  # The getter
    def ss_number(self):
        try:
            return self.__ss_number  # Note there are 2 underscores here
        except AttributeError:
            return "no social security number available"

    @property  # The getter
    def date_of_birth(self):
        try:
            return self.__date_of_birth  # Note there are 2 underscores here
        except AttributeError:
            return "no date of birth available"

    @property  # The getter
    def health_insurance_account_number(self):
        try:
            # Note there are 2 underscores here
            return self.__health_insurance_account_number
        except AttributeError:
            return "no health insurance account number available"
# address getter and setter
    @property  # The getter
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return "no address available"

    @address.setter  # The setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string value for the address')

    @property  # The getter
    def full_name(self):
        try:
            # Note there are 2 underscores here
            return f'{self.__first_name} {self.__last_name}'
        except AttributeError:
            return "enter a valid value for both first name and last name"


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
# cashew.ss_number = "838-31-2256"
# --> Produced AttributeError: can't set attribute! :)

# # Neither should this
# cashew.date_of_birth = "01-30-90"
# --> Produced AttributeError: can't set attribute! :)

# But printing either of them should work
print(f'Social Security Number: {cashew.ss_number}')
# --> This works! :)

# print(cashew.first_name)
# --> Produceed AttributeError:  'Patient' object has no attribute 'first name'
# print(cashew.last_name)
# --> Produceed AttributeError:  'Patient' object has no attribute 'last name'

print(cashew.full_name)   # "Daniela Agnoletti"

# cashew.address = 1024
# --> Produced TypeError:  Please provide a string value for the address :)

cashew.address = "1024 Getaway"

print(cashew.address)
# -->Printed 1024 Getaway
