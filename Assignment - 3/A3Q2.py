# Conversion of age in terms of Human Years to Dog Years

def human_to_Dog(human_year):

    if 0 <= human_year <= 2:
        dog_year = 10.5 * human_year

    else:
        dog_year = 21 + (4 * (human_year - 2))

    print(f'Age in Dog years is : {dog_year}')

human_year = float(input('Enter age in human years : '))
human_to_Dog(human_year)
