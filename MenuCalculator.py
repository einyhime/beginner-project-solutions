menu = ["", "Chicken Strips", "French Fries", "Hamburger", "Hotdog", "Large Drink", "Medium Drink", "Milk Shake", "Salad", "Small Drink"]
price = [0, 3.50, 2.50, 4.00, 3.50, 1.75, 1.50, 2.25, 3.75, 1.25]

print("---------------------")
print("MENU".center(20))
print("---------------------")
for i in range(1, len(menu)):
    print(f"{menu[i]} - ${price[i]}")

while True:
    total = 0
    order = input("\nEnter your order in numbers: ")
    print("YOU ORDERED:")
    order2 = list(set(order))

    for x in range(len(order2)):
        if order2[x] == '0':
            continue
        count = order.count(order2[x])
        temp = count * price[int(order2[x])]
        print(f"{menu[int(order2[x])]} : {count} (${temp})")
        total += temp

    print(f"Total : ${total}")
    
    check = input("\nAgain? Press Q to quit. ")
    if check == 'q':
        print("Thank you very much!")
        break