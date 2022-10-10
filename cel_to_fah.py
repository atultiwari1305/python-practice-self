from calendar import c
import string


temp=float(input("Enter your temperature: "))
unit=int(input("Enter the unit[c/f]: "))

if unit==0:
    print("Your temperature is: ", ((temp*1.8)+32),"f")
elif unit == 1:
    print("Your temperature is: ", ((temp-32)*(5/9)),"c")
else:
    print("WRONG INPUT!!!!!!!!!!")