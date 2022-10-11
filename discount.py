#discount of 10% if cost is more than 1000.

unit=int(input("Enter total units purchased: "))
rate=float(input("Enter the rate of one unit: "))

if unit*rate >= 1000:
    print("Net cost is: ",((unit*rate)-(0.1*unit*rate)))
else:
    print("Net cost is: ",unit*rate)
    