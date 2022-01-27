els = [0,1,3,6,10,15,21,28,35,45]


smallest_num = 2147483647
lnum = -2147483648
second_lnum = -2147483648
third_lnum = -2147483648

for i in els :
    if i > lnum:
        third_lnum = second_lnum
        second_lnum = lnum
        lnum = i
    elif i > second_lnum:
        third_lnum = second_lnum
        second_lnum = i
    elif i > third_lnum:
        third_lnum = i

    if i < smallest_num:
    	smallest_num = i


print("Largest number of the list is", lnum)
print("Smallest number of the list is", smallest_num)
print("Third largest number of the list is", third_lnum)
