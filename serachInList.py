import random
length_of_list = 10
searched_element = random.randint(0,20)
list_1 = list(random.randint(0,20) for i in range(length_of_list))

print(list_1)
print(searched_element)

if searched_element in list_1:
    print(f'Found {searched_element}!')

else:
    for i in range(20):
        if searched_element - i in list_1:
                print(f'The closest to the searched element found is {searched_element - i}.')
                break
        elif searched_element + i in list_1:
                print(f'The closest to the searched element found is {searched_element + i}.')
                break



