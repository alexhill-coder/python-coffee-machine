# A dictionary that stores the type of drink, its ingredients and the quantity it takes #
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

# Contains the total amount of resources available.
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

# A global variable used to store the inputted drink.
drink = "latte"

# Checks to see if there is enough ingredients to complete the order.


def check():
    index = 0
    for i in (MENU[drink]["ingredients"]):
        beverage = MENU[drink]["ingredients"][i]
        compare = resources[i]
        index += 1
        if beverage <= compare and index == 3:
            return True

        # Will start the loop again if ingredients are insufficient
        elif beverage > compare:
            print(f"Sorry there is not enough {i}.")
            machine()


def coins(drink_cost):

    # After the drink name is inputted the user is asked to provide various coins
    # as payment.
    print("Please insert coins.")
    quarters = float(input("how many quarters?: "))
    dimes = float(input("how many dimes?: "))
    nickles = float(input("how many nickles?: "))
    pennies = float(input("how many pennies?: "))

    # Check transaction was successful
    cost = drink_cost
    payment = round((0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies), 2)
    print(f"${payment:.2f}")

    # If enough money has been inputted it is added to the resource variable and returning true
    # If too much money has been inputted it will return the excess.
    if payment > cost:
        refund = payment - cost
        print(f"Here is ${refund:.2f} in change.")
        resources["money"] += cost
        return True
    elif payment == cost:
        print("Thanks for the exact payment")
        resources["money"] += cost
        return True

    # If not enough money has been inputted a message is outputted to indicate as such.
    # the program loop is started again.
    elif payment < cost:
        print("Sorry that's not enough money. Money refunded.")
        machine()

# On successful checking that enough ingredients are available the amount is
# deducted from the resources variable and the success message is outputted


def make(beverage, ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {beverage} ☕️. Enjoy!")

# Prompt the user by asking “What would you like?” to start the program.


def machine():
    global drink

    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    # Turn off the Coffee Machine by entering prompt off
    if drink == "off":
        print("Goodbye")
        exit()
    # Print a report of all the machines resources.
    elif drink == "report":
        print(f"Water: {resources['water']}ml\n"
              f"Milk: {resources['milk']}ml\n"
              f"Coffee: {resources['coffee']}g\n"
              f"Money: ${resources['money']:.2f}\n")
        machine()
    # Check resources are sufficient to make drink order.
    elif drink == "espresso" or "latte" or "cappuccino":
        if check() is True:
            # Process Coins
            if coins(MENU[drink]["cost"]) is True:
                # Make drink
                make(drink, MENU[drink]["ingredients"])
                machine()
    else:
        print("Sorry, can you repeat that")
        # The loop will continue until the program is stopped or off is inputted.
        machine()


machine()
