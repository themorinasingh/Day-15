def coin_counter(num_pennies, num_nickel, num_dime, num_quarter ):
    """Returns total money inserted"""
    penny = 0.01
    nickel = 0.05
    dime = 0.10
    quarter = 0.25

    return penny * num_pennies + nickel * num_nickel + dime * num_dime + quarter * num_quarter

resources = {
    "water": 500,
    "milk": 500,
    "coffee": 500,
    "money": 0.0
}

def transaction_handler(cost_of_drink, money_inserted):
    """Checks if the money inserted is enough to but the drink"""
    if cost_of_drink > money_inserted:
        return "Insufficient Amount, Money Refunded!!"
    elif cost_of_drink <= money_inserted:
        return f"Thank you for your order \nChange: {round(money_inserted - cost_of_drink, 2)}"

drink_requirements = {
    "espresso": {"milk": 0, "water": 50, "coffee": 18, "price": 1.50 },
    "latte" : {"milk": 150, "water": 200, "coffee": 24, "price": 2},
    "cappuccino": {"milk": 100, "water": 250, "coffee": 24, "price": 2 }
}

def drink_maker(drink_name):
    """prepares the drink if we have enough resources and update our resources and profit"""
    if resources["water"] >= drink_requirements[drink_name]["water"]:
        resources["water"] = resources["water"] - drink_requirements[drink_name]["water"]
        if resources["milk"] >= drink_requirements[drink_name]["milk"]:
            resources["milk"] = resources["milk"] - drink_requirements[drink_name]["milk"]
            if resources["coffee"] >= drink_requirements[drink_name]["coffee"]:
                resources["coffee"] = resources["coffee"] - drink_requirements[drink_name]["coffee"]
                resources["money"] = resources["money"] + drink_requirements[drink_name]["price"]
                return f"Here is your {drink_name}☕️. Enjoy!"

    else:
        return "Not Enough Resources, Money Refunded"

def report_generator(a_dict):
    return f"Water = {a_dict["water"]} \nMilk = {a_dict["milk"]} \nCoffee = {a_dict["coffee"]} \nMoney = {a_dict["money"]}"

machine_is_on = True

while machine_is_on:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink_choice == "off":
        machine_is_on = False
        print("Machine Turned Off")
        break
    elif drink_choice == "report":
        print(report_generator(resources))
        input("Press enter to continue")
        continue
    elif drink_choice == "cashout":
        resources["money"] = 0
        input("Cashed Out, press enter to continue")
    elif drink_choice == "restock":
        resources = {
            "water": 500,
            "milk": 500,
            "coffee": 500,
            "money": 0.0
        }

    number_of_pennies = int(input("Number Of Pennies: "))
    number_of_nickels = int(input("Number Of Nickels: "))
    number_of_dime = int(input("Number Of Dimes: "))
    number_of_quarters = int(input("Number Of Quarters: "))

    total_money_inserted = coin_counter(number_of_pennies,number_of_nickels, number_of_dime, number_of_quarters)
    print(transaction_handler(drink_requirements[drink_choice]["price"], total_money_inserted))
    if total_money_inserted > drink_requirements[drink_choice]["price"]:
        print(drink_maker(drink_choice))





