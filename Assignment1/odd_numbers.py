list1 = [1,2,3,4,5,6,7]
list2 = [8,9,10,11,12,13]
list3 = []


for num1 in list1:
    if num1 % 2 == 1:
        list3.append(num1)

for num2 in list2:
    if num2 % 2 == 1:
        list3.append(num2)

print(str(list3))