n = int(input("Enter the number of elements: "))
els = []
print("Enter", n, "numbers")
for i in range(n):
	els.append(int(input()))
search = int(input("Enter the number to search: "))
count = 0
for el in els:
	if el == search:
		count = 1
		break
if count == 0:
	print(search, "was not found the the list")
else:
	print(search, "was found the the list")
