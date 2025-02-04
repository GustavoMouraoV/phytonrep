### This program has been created to print flags based on user Input. Valids options are Greece - USA  - Italy  - France -- UK
def printFlag(flagname):

    width = input("Please input flag width:\n")
    width = int(width)
    height = input("Please input flag  height:\n")
    height = int(height)

    if flagname == 'Greece':
        print('Here is the flag of : ' + flagname)
        # Calculate half of the width and height fur use in multiplication
        half_width = int(width / 2)
        half_height = int(height / 2)

        # Create and print the rows of the flag
        upper_row = '#' * int(half_width/2)  + ' ' + '#' * int(half_width/2)+ '-' * half_width + '\n'
        middle_row =  ' ' * half_width +  '-' * half_width + '\n'
        lower_row = '-' * width + '\n'
        print(upper_row * int(half_height/2), end='')
        print(middle_row,end='')
        print(upper_row * int(half_height / 2), end='')
        print(lower_row * half_height, end='')
    else:
        print('Flag not available')

if __name__ == '__main__':
    flagname = input('Welcome to Flag Print. Please enter your flag:')
    printFlag(flagname)

