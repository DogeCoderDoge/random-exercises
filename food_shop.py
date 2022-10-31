start = input("Welcome to food shop, would you like to eat anything? ")
dishes = "1. Sushi $14 \n2. Noodles $8 \n3. Biryani $26 \n4. Salad $5"
cost = [14, 8, 26, 5]
total = 0

g = True

if start=="yes" or start=="y" or start=="":
    print(dishes)
    while g:
        item = int(input("What do you want to eat? "))
        total += cost[item-1]

        c = input("Do you want to eat anything else? ")
        if c == "no": g = False

    print("The price is $", total)

    
else: print("no food for you")
