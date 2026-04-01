# a= float(input("Enter the cost of the item : "))
# b = float(input("Enter the selling price of the item : "))
# if a > b:
#     print(f"The item is in sale and it is a profit of {a - b}")
# else:
#     print(f"The item is not in sale and it is a loss of {b - a}")
# n1 = int(input("Enter a natural number (n1) : "))
# o1 = input("Enter an operator (o1) [+, -, *]: ")
# n2 = int(input("Enter a natural number (n2) : "))
# o2 = input("Enter an operator (o2) [+, -, *]: ")
# n3 = int(input("Enter a natural number (n3) : "))
# if o1 == "+":
#     temp = n1 + n2
# elif o1 == "-":
#     temp = n1 - n2
# elif o1 == "*":
#     temp = n1 * n2
# else:
#     print("Invalid operator")
#     exit() #To break out of the Function when we get a invalid operator

# if o2 == "+":
#     print(f"Answer for operation : {temp + n3}")
# elif o2 == "-":
#     print(f"Answer for operation : {temp - n3}")
# elif o2 == "*":
#     print(f"Answer for operation : {temp * n3}")
# else:
#     print("Invalid operator")
#     exit()
# y1 = float(input("\nEnter the point of y1 : "))
# y2 = float(input("Enter the point of y2 : "))
# y3 = float(input("Enter the point of y3 : "))
# x1 = float(input("Enter the point of x1 : "))
# x2 = float(input("Enter the point of x2 : "))
# x3 = float(input("Enter the point of x3 : "))
# slope1 = ((y2 - y1)/(x2 - x1))
# slope2 = ((y3 - y2)/(x3 - x2))
# if slope1 == slope2:

#     print(f"\nIt is a straight line {slope1, slope2}\n")
# else:
#     print("\nIt is not a straight line\n")
# a = int(input("Enter a number : "))
# if a & 1 == 0:
#     print(f"Remainder is 0 and quotient is {a>>1}")
# else:
#     print(f"Remainder is {a & 1} and quotient is {a>>1}")
# hard = int(input("Enter the hard of the steel : "))
# carbon = float(input("Enter the carbon content of the steel : "))
# tens = int(input("Enter the tensile strength of the steel : "))
# if hard > 50 and carbon < 0.7 and tens > 5600:
#     print("Grade 10 Steel")
# elif hard > 50 and carbon < 0.7:
#     print("Grade 9 Steel")
# elif carbon < 0.7 and tens > 5600:
#     print("Grade 8 Steel")
# elif hard > 50 and tens > 5600:
#     print("Grade 7 Steel")
# elif hard > 50 or carbon < 0.7 or tens > 5600:
#     print("Grade 6 Steel")
# else:
#     print("Grade 5 Steel")
