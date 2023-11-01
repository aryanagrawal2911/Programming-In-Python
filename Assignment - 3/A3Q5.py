def check_decibel(n):

    if n < 40:
        print('Sound Value quieter than Quiet Room.')

    elif n == 40:
        print('Sound Value of Quiet Room.')

    elif 40 < n < 70:
        print('Sound Value between Quiet Room and Alarm Clock.')

    elif n == 70:
        print('Sound Value of Alarm Clock.')

    elif 70 < n < 106:
        print('Sound Value between Alarm Clock and Gas Lawnmower.')

    elif n == 106:
        print('Sound Value of Gas Lawnmower.')

    elif 106 < n < 130:
        print('Sound Value between Gas Lawnmower and Jackhammer.')

    elif n == 130:
        print('Sound Value of Jackhammer.')

    else:
        print('Sound Value louder than Jackhammer.')

sd = float(input('Enter sound value in decibels : '))
check_decibel(sd)

    
