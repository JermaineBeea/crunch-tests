"""
STEP 1: Fix the declaration of the functions below to get the 
tests in test_functions.py to run.
"""

def get_date_of_birth(id_number): 
    """
    STEP 2: Extract the date of birth from the ID number and return it as a string
    """
    #todo

    date_of_birth = []
    for indx in range(3):
        date_of_birth.append(id_number[2 * indx: 2 * (indx + 1)])

    return '/'.join(date_of_birth[::-1])


def get_gender(id_number):
    """
    STEP 3: Extract the gender from the ID number using the formula below and return
    it as a string

    Formula: 1 if the ID number's 7th to 10th digit is less than 5000, the person is
    female and if it is greater than 4999, the person is male.
    """
    #todo
    if int(id_number[6: 10]) > 4999:
        return 'Male'
    else:
        return 'Female'

def get_citizenship(id_number):
    """
    STEP 4: Extract the citizenship from the ID number using the formula below and 
    return it as a string

    Formula: 1 if the ID number's 11th to 12th digit is less than 01, the person is
    a South African citizen and if it is greater than 01, the person is a non-South 
    African citizen.
    """
    #todo
    if int(id_number[10]) == 0 :
        return 'South African'
    else:
        return 'Non-South African'

