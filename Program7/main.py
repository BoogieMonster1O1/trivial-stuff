a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

disc = b**2 - 4*a*c
x1 = (-b + disc**0.5)/(2*a)
x2 = (-b - disc**0.5)/(2*a)
print("Roots: ", x1, x2)
