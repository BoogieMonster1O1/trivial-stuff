els = [1,3,5,7,9]
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
