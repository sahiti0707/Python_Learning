# To count number of positive numbers
list1 = [-10, -21, -4, -45, -66, 93, 11]
print(list1)

pos_count, neg_count = 0, 0
num = 0


while(num < len(list1)):

    if list1[num] >= 0:
        pos_count += 1
    else:
        neg_count += 1

    num += 1

print("Positive numbers in the list: ", pos_count)
print("Negative numbers in the list: ", neg_count)
