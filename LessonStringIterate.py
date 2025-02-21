#This is a Phyton lesson about string iteration

def iterate():
    string = 'The big Brow Mamoth'
    for char in string:
        print(char)

def validatephone():
    phone = input('Enter your phone number: ')
    if len(phone) != 11:
        print('Invalid phone number!')
    elif phone[3] != '-' or phone[7] != '-':
        print('Invalid phone number!')
    elif phone.isdigit():
        print('Valid phone number!')

def validatephone2():
    phone = input('Enter your phone number: ')
    for i in range(0,len(phone)):
        if phone[3] != '-' and  phone[7] != '-':
            print('Invalid phone format!')
            break
        elif i != 3 and i != 6 and phone[i].isdigit() == False:
            print ('Phone is not digit!')
            break
        elif len(phone) != 11 :
            print('Invalid phone lenght!')
            break
        else :
            print('Valid phone number! Thank you!')
            exit()

if __name__ == '__main__':
    print('String Iterate Lesson')
    #iterate()
    #validatephone()
    validatephone2()
