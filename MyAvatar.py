#This script will create a character avatar based on user inputs

#Print the Head of the Avatar
def print_head(hair,eyes):
    print('')
    print(hair * 10)
    print(hair + '|' + (' ' * 6) + '|' + hair )
    print(hair + '|' + ' ' + eyes + '  ' + eyes + ' ' +'|' + hair)
    print(' ' + '|' + '  '+'#'+ '   '+'|'+' ')
    print(' ' + '|' + (' ' * 6) + '|' + ' ')
    print(' \ \'--\' /')
    print('  '+ ('-' * 6))

#Print the torso of the avatar according to defined height
def print_body(height,hand):
    print((' ' * 4) + 'XX' + (' ' * 4))
    print(hand + '|' + ('=' * 2) + '##' +  ('=' * 2) +  '|' + hand )
    print((' ' * 4) + ('XX'))
    i = 4
    for index in range(1,height):
        if (index <= i):
            print((' ' * i) + ('XX' * index))
            if (i > 0):
                i = i - 1
        else:
            print('  '+ ('X' * 6))

#Revert the shoe string for right shoe
def reverse_shoe(shoe_string):
    return shoe_string[::-1]

##Print legs with both shoe and reversed shoe
def print_legs(shoe,reversed):
    print((' ' * 3) + ('=' * 4))
    for index in range(0,3):
        print ((' ' * 2) + '|' + '' + '|' + '  ' +  '|' +  '' + '|')
    print(shoe + '  ' + reversed)


def main ():
    print("Welcome to MyAvatar")
    height = int(input("Please inform the height of your avatar: "))
    hair = input("Please choose a character for the hair of your avatar: ")
    eyes = input("Please choose a character for the eyes of your avatar: ")
    hand = input("Please choose a character for the hand of your avatar: ")
    shoe = input("Please choose four characters for the shoes of your avatar: ")
    reversed= reverse_shoe(shoe)
    #segment = (height - 11) // 2
    print_head(hair,eyes)
    print_body(height,hand)
    print_legs(shoe,reversed)


main()