n = int(input("Enter number of terms: "))
a = 0
b = 1
print(a, end=' ')
for i in range(1, n):
	print(b, end=' ')
	c = a + b
	a = b
	b = c

print()

