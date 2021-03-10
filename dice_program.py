def dice_roll():
    import random
    if input('Would you like to roll the dice? y/n ') == 'y':
        while True:
            print('The dice says: ' + str(random.randint(1,6)) + '\n')
            if input('Would you like to roll again? y/n ') == 'y':
                continue
            else:
                print('\nThanks for playing!')
                break
    else:
        print('Fine, have it your way!')

dice_roll()