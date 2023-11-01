# Taking month name as input and giving the number of days in it

def check_days(m):

    if (m == 'APRIL') or (m == 'JUNE') or (m == 'SEPTEMBER') or (m == 'NOVEMBER'):
        print(f'{m} has 30 days.')

    elif m == 'FEBRUARY':
        print(f'{m} has 29 days in case of a leap year, else it has 28 days.')

    else:
        print(f'{m} has 31 days.')

month = input('Enter the month : ').upper()
assert month in ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']
check_days(month)
