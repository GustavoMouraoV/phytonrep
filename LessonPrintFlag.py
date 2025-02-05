### This program has been created to print flags based on user Input. Valids options are Greece - USA  - Italy  - France -- UK

def printFlag(flagname):

    width = input("Please input flag width:\n")
    width = int(width)
    height = input("Please input flag  height:\n")
    height = int(height)
    half_width = int(width / 2)
    half_height = int(height / 3)
    third_width = int(width / 3)
    third_height = int(height / 3)

    if flagname.upper() == 'GREECE':
        print('Here is the flag of : ' + flagname)
        # Calculate half of the width and height for use in multiplication
        # Create and print the rows of the flag
        upper_row = '#' * int(half_width/2)  + ' ' + '#' * int(half_width/2)+ '-' * half_width + '\n'
        middle_row =  ' ' * half_width +  '-' * half_width + '\n'
        lower_row = '-' * width + '\n'
        print(upper_row * int(half_height/2), end='')
        print(middle_row,end='')
        print(upper_row * int(half_height / 2), end='')
        print(lower_row * half_height, end='')

    elif flagname.upper() == 'USA':
        print('Here is the flag of : ' + flagname)
        upper_row = '#' * int(half_width) + '-' * half_width + '\n'
        lower_row = '-' * width + '\n'
        print(upper_row * int(half_height), end='')
        print(lower_row * half_height, end='')

    elif flagname.upper() == 'ITALY':
        print('Here is the flag of : ' + flagname)
        upper_row = '#' * int(third_height) + '~' * third_height + '#' * int(third_height) + '\n'
        print(upper_row * int(height), end='')
    else:
        print('Flag not available!')


if __name__ == '__main__':
    flagname = input('Welcome to Flag Print. Please enter your flag:')
    printFlag(flagname)

