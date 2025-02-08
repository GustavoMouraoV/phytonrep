#Phyton Script to Vizualizing Finnances - Portugal 2025
def get_expenses () :
    anualincome = input("Please.Enter your anual income: ")
    monthexpense = input("Please.Enter your monthly expense: ")
    monthrent = input("Please.Enter your monthly rent: ")
    weekfood = input("Please.Enter your weekly food expense: ")
    yearvacations = input("Please.Enter your yearly vacations expense: ")

    if  (anualincome.isnumeric() == False)  :
        print('Invalid anual income!')
    elif (monthexpense.isnumeric()  == False)   :
        print('Invalid Month expense value!')
    elif (monthrent.isnumeric() == False)   :
        print('Invalid Mont rent value!')
    elif (weekfood.isnumeric() == False) :
        print('Invalid week food expense!')
    elif (yearvacations.isnumeric() == False) :
        print('Invalid Year vacations expense!')
    else :
        print('All valid values. Thank you!')
        vartax = set_taxes(anualincome)
        print('They will charge you with Tax : ' + str(vartax))
        varmonthexpense  = round(float(monthexpense * 12),2)
        varmonthrent = round(float(monthrent * 12),2)
        varweekfood = round(float(weekfood * 52), 2)
        varyearvacations = round(float(yearvacations), 2)


        annual_extra = int(anualincome) - int(varmonthrent) - int(varmonthexpense) - int(varweekfood) - int(varyearvacations) - int(vartax)

        percentage_tax = round((vartax / float(anualincome)) * 100, 1)
        print('Your Year General expense is : ' + str(varmonthexpense))
        print('Your Year Rent is : ' + str(varmonthrent))
        print('Your Year Food Expense is : ' + str(varweekfood))
        print('Your Year Vacations Expense is : ' + str(varyearvacations))

        percentage_housing = round((varmonthrent / float(anualincome)) * 100, 1)
        percentage_bills = round((varmonthexpense / float(anualincome)) * 100, 1)
        percentage_food = round((varweekfood / float(anualincome)) * 100, 1)
        percentage_travel = round((varyearvacations / float(anualincome)) * 100, 1)
        percentage_extra = round((annual_extra / float(anualincome)) * 100, 1)

        # Display the grid with financial information and bar chart

        print('Your Year General percent expense is : ' + str(percentage_housing))
        print('Your Year Rent percent expense is : ' + str(percentage_housing))
        print('Your Year Food percent expense is : ' + str(percentage_food))
        print('Your Year Vacations percent expense is : ' + str(percentage_extra))
        print('Your Year Extra saving is : ' + str(percentage_tax))


def set_taxes (income) :
    incometx = float(income)
    taxvar = 0
    if (incometx <= 10000) :
        taxvar =  round(incometx * 0.05, 2)
        print('Your income tax amount: ' + str(taxvar) + ' with a rate of 5%')
    elif (incometx > 10000 and incometx <= 40000) :
        taxvar =  round(incometx * 0.1, 2)
        print('Your income tax is amount: ' + str(taxvar) + ' with a rate of 10%')
    elif (incometx > 40000 and incometx <= 80000) :
        taxvar = round(incometx * 0.15, 2)
        print('Your income tax is amount: ' + str(taxvar) + ' with a rate of  15%')
    elif (incometx > 80001) :
        taxvar = round(incometx * 0.20, 2)
        print('Your income tax is amount: ' + str(taxvar) + ' with a rate of  20%')
    else :
        print('Your right dude!')

    return taxvar

if __name__ == '__main__':
    print('Welcome to Fynnance Vizualizer Portugal - 2025!')
    get_expenses()
