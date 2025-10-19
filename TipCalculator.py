#tip percentage

def tip_calc (tip_perc, bill):
    return tip_perc * bill / 100

tip_percent = float(input("Enter the tip percentage (%): "))
bills_dollars = float(input("Enter the bill amount ($): "))