products = ["iphon 15","samsoung s24","xiomie poco","samsoung a15"]
price = [8500000,7000000,2500000,1500000]
great = print("welcome! to our shop!")
sabad = []
cart = 0
for i in products:
    print(i,"price: ",price[products.index(i)])
while True:
    order = input("enter your order:  ")
    if order in products:
        print("done!")
        sabad.append(order)
        cart += price[products.index(order)]
    
    else: 
        print("no products found ")
    command = input("do you want to continu: (y/n)")
    if command=="y":
        continue
    else:
        break
if cart > 0:
    for i in sabad:
        print(i)
    print("total: ",cart)
    final = input("1.pay , 2.cancel :  ")
    if final=="pay":
        print("thanks for your shoping")
    if final=="cancel":
        print("")
