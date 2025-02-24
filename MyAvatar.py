#This script will create a character avatar based on user inputs

def print_head(hair,eyes):
    print('')
    print(hair * 10)
    print(hair + '|' + (' ' * 6) + '|' + hair )
    print(hair + '|' + ' ' + eyes + '  ' + eyes + ' ' +'|' + hair)
    print(' ' + '|' + '  '+'#'+ '   '+'|'+' ')
    print(' ' + '|' + (' ' * 6) + '|' + ' ')
    print(' \ \'--\' /')
    print('  '+ ('-' * 6))



def main ():
    print("Welcome to MyAvatar")
    #height = int(input("Please inform the height of your avatar: "))
    hair = input("Please choose a character for the hair of your avatar: ")
    eyes = input("Please choose a character for the eyes of your avatar: ")
    #hand = input("Please choose a character for the hand of your avatar: ")
    #shoe = input("Please choose four characters for the shoes of your avatar: ")
    #segment = (height - 11) // 2
    print_head(hair,eyes)


main()