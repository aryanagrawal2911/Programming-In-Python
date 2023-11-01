# Desired value Assignment with single Control statemant

def grade(n):
    rem = 'average'

    if n >= 70:
        rem = 'good'

    print(rem)

marks = float(input('Enter marks : '))
grade(marks)
