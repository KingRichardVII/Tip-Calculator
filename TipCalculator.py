# Richard Phan
# 10/20/25

def tip_calc ():
    tip_percent = float(input("Enter the tip percentage (%): "))
    bill_dollars = float(input("Enter the bill amount ($): "))
    tip_amount = tip_percent * bill_dollars / 100
    print('Your tip  should be $' + str(tip_amount))
    print('Your bills should be $' + str(tip_amount + bill_dollars))

tip_calc()

#Add input validation
    #do not accept characters
    #do not accept letters
    #do not accept negative numbers

#add interface app (front end)



