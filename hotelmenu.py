#define the menu of restaurant
menu = {
    'Pizza' : 100,
    'Pasta' : 40,
    'Burger' : 60,
    'Tea' : 10,
    'Coffee' : 30,
    'Salad' : 50,
    'Fries' : 40,
    'Noodles': 60,
    'Cookiee': 50,
    'Sauce': 10,    
}

#greet
print("welcome to This restaurant")
print("Pizza : Rs100\nPasta : Rs40\nBurger : Rs60\nTea : Rs10\nCoffee: Rs30\nSalad: Rs50\nFries : Rs40\nNoodles: Rs60\nCookiee: Rs50\nSauce: Rs10 ")

order_total = 0

item_1 = input("enter the name of item you want to order =")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"ordered item { item_1} is not available yet !")

another_order = input("Do you want to add another item? (yes/ no)")
if another_order == "yes":
    item_2 = input("Enter name of your Second item = ")
    if item_2 in menu:
        order_total += menu [item_2]
        print(f"item {item_2} has been ordered")
    else:
        print(f"ordered item {item_2} is not available!")
        
print(f"total amount of items to pay is {order_total}")


