print("HELLO USER")
a=float(input("Enter the coefficient of x2: "))
b=float(input("Enter the coefficient of x: "))
c=float(input("Enter the constant value: "))

if a==0:
    print("NOT A QUADRATIc EQUATION.")
elif ((b**2) - (4*a*c)) == 0:
    print("THE EQUATION HAVE TWO EQUAL ROOTS.")
    print("x1 = x2 = ",(-b/(4*a)))
elif ((b**2) - (4*a*c)) > 0:
    print("THE EQUATION HAVE TWO DISTINcT ROOTS.")
    print("x1 = ",((-b+((b**2) - (4*a*c))**0.5)/(2*a)), "AND" ,"x2 = ",((-b-((b**2) - (4*a*c))**0.5)/(2*a)))
else:
    print("THE EQUATION HAVE NO REAL ROOTS.")