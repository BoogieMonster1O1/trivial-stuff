els = [1,2,3,3,4,4,4,4,5,5,5,6,6]
search = int(input("Enter the number to search: "))
count = 0
for el in els:
	if el == search:
		count += 1
print(search,"occurred in the list",count,"times")
