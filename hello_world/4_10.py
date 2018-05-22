foods = ['pizza','falafel','carrot cake','cannoli','ice cream']
cp_foods = foods[:]
cp_foods.append('tofu')
length = len(foods)
i = int(length/2) - 1
print("The first three items in the list are:")
for food in foods[:3]:
    print(food)
print("\nThree items from the middle of the list are:")
for food in foods[i:i+3]:
    print(food)
print("\nThe last three items in the list are:")
for food in foods[-3:]:
    print(food)
print(cp_foods)
# print(food for food in foods[:3])