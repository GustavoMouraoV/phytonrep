## Welcome to sing up form validator, this is lesson to validate forms and functions declarations
def validatemail(email):
    at_count = 0
    dot_count = 0
    for character in email:
        if character == '@':
            at_count += 1
        if character == '.':
            dot_count += 1
    return at_count == 1 and dot_count >= 1

def validatephone(phone):
    for i in range(0,len(phone)):
        if phone[3] != '-' and  phone[7] != '-':
            print('Invalid phone format!')
            return False
        elif i != 3 and i != 6 and phone[i].isdigit() == False:
            print ('Phone is not digit!')
            return False
        elif len(phone) != 11 :
            print('Invalid phone lenght!')
            return False
        else :
            return True

def main():
    print("Welcome to the sign-up form.")
    print("Please provide your email and phone number so we can contact you.")

    phonein = input("Phone number: ")
    emailin = input("Email Address: ")

    validatephone(phonein)
    validatemail(emailin)

    if validatephone and validatemail:
        print("Email and Phone are valid.Thanks for providing your information!")
    else:
        print("Something is not right. Please try again.")

main()