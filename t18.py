pizza = 200
dizi = 260
burger = 160
kobedie = 170
sorat_hesab = 0
while True:
    order = input('enter your order: ')
    if order=='pizza':
        sorat_hesab+=pizza
    elif order=='dizi':
        sorat_hesab+=dizi
    elif order=='burger':
        sorat_hesab+=burger
    elif order=='kobedie':
        sorat_hesab+=kobedie
    else:
        print('invalid order')
    command = input('do you want to continue (y/n) :  ')
    if command=='y':
        continue
    else:
        break
print('sorat_hesab:',sorat_hesab)
