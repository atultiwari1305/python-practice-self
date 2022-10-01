#area of any triangle

a=float(input("Enter your first side:"))
b=float(input("Enter your Second side:"))
c=float(input("Enter your Third side:"))

s = (a + b + c) / 2

area= (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of triangle is: ", area)