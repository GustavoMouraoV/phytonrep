###Phyton Script to calculate Number Divisibility

def dividebynumber(mynumber):
    print('You choose the number: ' + str(mynumber))
    start = int(input('What value should we start at? '))
    end = int(input('What value should we end at? '))
    number = start
    while number <= end:
        if number % mynumber == 0:
            print(number, 'is divisible by', mynumber)
        number += 1

if __name__ == '__main__':
    pexit = bool(False)
    while pexit == False:
        mynumber = int(input("Welcome to Divisibility Calculator. Please Enter a number: "))
        if mynumber == 0 :
            print('You did not enter a number.')
            if int(input('Press 1 to Exit or 0 To continue: '))== 1  :
                pexit = True
            else:
                pexit = False
        else:
             dividebynumber(mynumber)
             if int(input('Press 1 to Exit or 0 To continue: ')) == 1:
                 pexit = True
             else:
                 pexit = False