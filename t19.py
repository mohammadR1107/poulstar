menu = input('add , edit , delet , :  ')
list_cars = ['bmw','benz','ford','saipa','lamborgini']
print(list_cars)
if menu=='add':
    list_cars.append(input('add your favorite car to the list: '))
elif menu=='delet':
    list_cars.remove(input('delet the one of the car in the list'))
elif menu=='edit':
    list_cars[int(input('enter number of car do you want to edit'))] = input('enter name of the new car')
print(list_cars)

