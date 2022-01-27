str = input("Enter the line: ")
alphabets = 0
upper = 0
lower = 0
digits = 0
for ch in str:
	if ch.isdigit():
		digits += 1
	elif ch.isalpha():
		alphabets += 1
		if ch.isupper():
			upper += 1
		elif ch.islower():
			lower += 1

print("Alphabets: ", alphabets)
print("Uppercase letters: ", upper)
print("Lowercase letters: ", lower)
print("Digits: ", digits)

