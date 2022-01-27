str = input("Enter the word: ")
vow = 0
cons = 0
for ch in str:
	if ch.isalpha():
		low = ch.lower()
		if low == "a" or low == "e" or low == "i" or low == "o" or low == "u":
			vow += 1
		else:
			cons += 1
print("Vowels:", vow)
print("Consonants:", cons)

