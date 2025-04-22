import random
names = []
num_of_names = int(input('enter number of names: '))
for i in range(num_of_names):
    name=input('enter the name: ')
    names.append(name)
winners = random.sample(names,3)
print(f"first winner: {winners[0]}")
print(f"second winner:  {winners[1]}")
print(f"third winner: {winners[2]}")
    
    