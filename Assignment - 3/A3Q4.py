# Payout Program for Casino Roulettes

import random
import sys

def payout(n):

    black = {1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36}

    if n == 37:
        print('The spin resulted in 00')

    else:
        print(f'The spin resulted in {n}')

    if n == 37:
        print('Pay 00')
        sys.exit()

    if n == 0:
        print(f'Pay {n}')
        sys.exit()

    print(f'Pay {n}')

    if (n % 2) == 0:
        print('Pay Even')

    else:
        print('Pay odd')

    if 1 <= n <= 18:
        print('Pay 1 to 18')

    else:
        print('Pay 19 to 36')

    if n in black:
        print('Pay Black')

    else:
        print('Pay Red')

payout(random.randint(0, 37))
