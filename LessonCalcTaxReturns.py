##This lesson has as objective to calculate the tax value with multiple return values for functions
##Validate the inputs values
def validateval(income,deduction):
    if income < deduction:
        print('The income can not be less than the deduction')
        return False
    elif income.isdigit() == False or deduction.isdigit() == False:
        print('The income or deduction values are invalid!Please review')
        return False
    else :
        print('Valid inputs, proceeding with calculations...')
        return True
## Calculate the tax percentage based on income amount
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
        taxvar = round(incometx * 0.20, 2)
        print('Your income tax is amount: ' + str(taxvar) + ' with a rate of  20%')
    elif (incometx > 80001) :
        taxvar = round(incometx * 0.25, 2)
        print('Your income tax is amount: ' + str(taxvar) + ' with a rate of  25%')
    return taxvar
## Calculate the final tax value
def caltax(income,deduction):
    taxamount = set_taxes(income)
    taxfinal = taxamount - float(deduction)
    liquidincome = float(income) - taxfinal
    return taxamount,taxfinal,liquidincome

def main():
    income = input("Please inform your annual income:")
    deduction = input("Please inform your annual deduction:")
    if (validateval(income,deduction)):
        taxamount,taxfinal,incomefinal = caltax(income,deduction)
        print('Your brute income tax amount is: ' + str(taxamount))
        print('Your tax amount after deduction is: ' + str(taxfinal))
        print('Your remaining income after tax is : ' + str(incomefinal))
    else :
        ('Your inputs are not valid.Please try again!')

main()