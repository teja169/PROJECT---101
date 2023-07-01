import random

dice_faces = [
    '''
    ---------
    |       |
    |   1   |
    |       |
    ---------
    ''',
    '''
    ---------
    | 2     |
    |       |
    |     2 |
    ---------
    ''',
    '''
    ---------
    | 3     |
    |   3   |
    |     3 |
    ---------
    ''',
    '''
    ---------
    | 4   4 |
    |       |
    | 4   4 |
    ---------
    ''',
    '''
    ---------
    | 5   5 |
    |   5   |
    | 5   5 |
    ---------
    ''',
    '''
    ---------
    | 6   6 |
    | 6   6 |
    | 6   6 |
    ---------
    '''
]

def roll_dice():
    while True:
        choice = input("Press Enter to roll the dice or 'N' to exit: ").upper()
        if choice == 'N':
            break
        elif choice == '':
            dice_value = random.randint(1, 6)
            print(dice_faces[dice_value - 1])

roll_dice()
