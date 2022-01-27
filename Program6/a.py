x = int(input("Enter a number: "))

other_factors = 0

for i in range(2, int(x**0.5) + 1):
	if x % i == 0:
		other_factors += 1
		break

if other_factors == 0:
	print("The number is prime")
else:
	print("The number is not prime")

