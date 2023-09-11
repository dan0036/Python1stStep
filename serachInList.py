import random
lengthOfList = 10 #int(input('Enter a length of the list: '))
searchedElement = random.randint(0,100) #int(input('Enter a length of the list: '))
list_1 = list(random.randint(0,100) for i in range(lengthOfList))

print(list_1)
print(searchedElement)
found = False
for i in list_1:
    if i == searchedElement:
        print(f'Searched element found on the {list_1.index(searchedElement)} position')
        found = True
        break

if found == False:
    for i in range(100):
        for j in list_1:
            if j - i == searchedElement and found == False:
                print(f'The closest to the searched element is {j}, found on the {list_1.index(searchedElement+i)} position')
                found = True
            if j + i == searchedElement and found == False:
                print(f'The closest to the searched element is {j}, found on the {list_1.index(searchedElement-i)} position')
                found = True




