number = []
for i in range(10):
        num = int(input('enter number: '))
        number.append(num)
number.sort()
print(number)
max_number = max(number)
print(max_number)
min_number = min(number)
print(min_number)