"""
Name: Madison Stehle
Armstrong Number Calculator:
Obtains a number n from the user that is greater than or equal to 10 and less than or equal to 100,000,000
Then determines all Armstrong numbers from 10 through n.
"""


def get_data():
    num = int(input(
        '\nWelcome to the Armstrong number calculator. \nPlease enter an integer from 10 through 100,000,000 (without '
        'the commas): '))

    while num < 10 or num > 100000000:
        print('ERROR! Input must be a whole number between 10 and 100,000,000')

        num = int(input('Please enter an integer from 10 through 100,000,000 (without the commas): '))

    return num


def calculate_armstrong_num():
    num = get_data()
    count = 0

    print(f'\nThe Armstrong numbers from 10 through {num} are:\n')

    for i in range(10, num + 1):
        num_array = [int(d) for d in str(i)]
        total = 0

        for j in range(0, len(num_array)):
            total += num_array[j] ** len(num_array)

        if i == total:
            print(i)
            count += 1

    print(f'\nThe total number of Armstrong numbers found was {count}')


calculate_armstrong_num()
