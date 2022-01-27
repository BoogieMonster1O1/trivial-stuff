n = int(input("Enter the value of n: "))
x = float(input("Enter the value of x: "))

sum = 0

for i in range(n + 1):
	fact = 1
	for num in range(1, i + 1):
		fact *= num
	sum += x**i / fact

print("e^x = ", sum)
