

appetizers = ['Wings','Cookies','Spring Rolls']
entress = ['Salmon','Steak','Meat','A literal Garden']
desserts = ['Ice Cream','Cake','Pie']
drinks = ['Coffee','Tea','Unicorn Tears']

def menu_print():
    print("Appetizers")
    print("-------")
    for i in appetizers:
        print(i)
    print("")

    print("Entrees")
    print("-------")
    for i in entress:
        print(i)
    print("")

    print("Desserts")
    print("-------")
    for i in desserts:
        print(i)
    print("")

    print("Drinks")
    print("-------")
    for i in drinks:
        print(i)
    print("")


def order():
    x = []
    while True:
        meal = input(">")
        if meal == "quit":
            print("You orderd")
            print('\n')
            break
        else:
            x.append(meal)
            counting = x.count(meal)
            print('\n')
            print(f'** {counting} orders of {meal} have been added to your meal **')
            print('\n')

print("$ python snakes_cafe.py")
print("**************************")
print("** Welcome to the Snakes Cafe! **")
print("** Please see our menu below. **")
print("**")
print("To quit at any time, type 'quit' **")
print("**************************")

menu_print()

print("**************************")
print("** What would you like to order? **")
print("**************************")

order()
