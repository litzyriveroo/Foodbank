# This project will help simplify the documentation of cases for the FoodBank.
import re      # this is needed to use regex
import random

def main():
    case_numbers = get_case_numbers()
    number_of_cases_wanted = get_user_input()

    # Depending on the number of cases wanted it will return random cases from the list.
    cases = random.sample(case_numbers, number_of_cases_wanted)

    for case in cases:
        print(case)


def get_user_input():
    """This function checks whether the inputted value is an int or not."""

    number_of_cases_wanted = int(input('How many cases would you like to report? '))

    while not isinstance(number_of_cases_wanted, int):
        number_of_cases_wanted = input('How many cases would you like to report? Please enter a number. ')

    return number_of_cases_wanted


def get_case_numbers():
    case_numbers = []
    pattern = r'^C\d{6}$'  # This regex will search each line for C123456

    case_file = open(".venv/lib/Food_Bank_Cases.txt", 'r')
    content = case_file.readlines()

    for line in content:
        line = line.strip()  # This will strip all whitespaces

        if re.match(pattern, line):
            case_numbers.append(line)

    return case_numbers


if __name__ == "__main__":
    main()
