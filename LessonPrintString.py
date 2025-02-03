# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.

    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    print('My name is Gus.')
    var_name = input('What is your name? ')
    print(f'Nice to meet you: {var_name}')
    var_age = input('How old are you? ')
    print(f'{var_name} is ' + str(var_age) + ' years old.')

def calc_profit():
    revenue = int(input('Please input your business revenue: '))
    cost   = int(input('Please input your business cost: '))
    profit = revenue - cost
    print('Your profit is : ' + str(profit))
    cost_bar = '#' * cost
    profit_bar = '#' * revenue
    print('Cost : ' + cost_bar)
    print('Profit: ' + profit_bar)
    print('Pycharm Graphics')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calc_profit()
    #print_hi('PyCharmm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
