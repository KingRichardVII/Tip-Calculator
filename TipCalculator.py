#tip percentage

def tip_calc (tip_perc, bill):
    return tip_perc * bill / 100

tip_percent = float(input("Enter the tip percentage (%): "))
bill_dollars = float(input("Enter the bill amount ($): "))

tip_amount = tip_calc(tip_percent, bill_dollars)

print('Your tip  should be $' + str(tip_amount))
print('Your bills should be $' + str(tip_amount + bill_dollars))