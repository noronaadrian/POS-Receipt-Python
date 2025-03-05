import datetime

print("============ Munch Craze Mix 'n Match =============")
print("Main")
print("m1: McSpaghetti")
print("m2: Cheesy Burger")
print("m3: Chicken Fillet Ala King")
print("===================================================")
print("Adds on")
print("p1: McCafe")
print("p2: McFloat")
print("p3: Sundae")
print("FOR ONLY 75 pesos!!!!")


def calculate_discount(total, discount):
    return total * discount


def print_receipt(order, total_cost, money_paid, change, discounted, vat_amount, is_senior):
    print("\n*************** Receipt ***************")
    print("")
    print("        Munch Craze Mix 'n Match")
    print("         Thank you for eating")
    print("")
    print("==========================================")
    print("Date and Time: {}".format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    print("Adress: CvSU Imus, Cavite")
    
    if is_senior:
        print("Senior Citizen or PWD: Yes")
        print("Total of discount:", round(discounted))
        print("==========================================")
    else:
        print("Senior Citizen or PWD: No")
        print("")
    if order:
        print("Your order:")
        for item, quan in order.items():
            print(f"{item} x{quan}")
        
        print("\nVAT:", round(vat_amount))
        
    print("Total Cost: ", total_cost)
    print("Money paid: ", money_paid)
    
    if money_paid:
        print(f"Change: {change:.2f}")
    
    print("****************************************")
    print("\nThank you for buying!!! 😊")

# Main menu items
main_menu = {
    "m1": "McSpaghetti",
    "m2": "Cheesy Burger",
    "m3": "Chicken Fillet Ala King"
}

# Adds on items
adds_on_menu = {
    "p1": "McCafe",
    "p2": "McFloat",
    "p3": "Sundae"
}
order = {}
price = 75
senior_citizen_discount = 0.2
def take_order(main_menu, adds_on_menu):
 while True:

    main_choice = input("Choose your main (type 'done' if you're finished): ")
  
    if main_choice == "done":
        break
  
    if main_choice not in main_menu:
        print("Invalid choice. Please try again.")
        continue
    adds_on_choice = input("Choose your add-on: ")

    if adds_on_choice not in adds_on_menu:
        print("Invalid choice. Please try again.")
        continue

    quantity = int(input("Enter the quantity '-1' to cancel your order  : "))

    item_name = f"{main_menu[main_choice]} + {adds_on_menu[adds_on_choice]}"

    if item_name in order:
        order[item_name] += quantity
    if quantity < 0:
     for void in item_name:
         void = order.pop
     print("You canceled ", item_name)
    else:
        order[item_name] = quantity  
take_order(main_menu, adds_on_menu)

total_cost = price * sum(order.values())

vat = total_cost * 0.12

total_cost = vat + total_cost

while True:
    is_senior = input("Do you have Senior Citizen or PWD card? (yes/no) ")
    if is_senior == 'yes':
        discounted = calculate_discount(total_cost, senior_citizen_discount)
        total_cost -= discounted
        break
    if is_senior == 'no':
        total_cost
        break
    else:
        print("Invalid input") 
        continue

print("\nTotal amount of your order", total_cost)

while True:
 money_paid = int(input("Enter the amount paid by the buyer: "))
 if money_paid < total_cost:
    print("Insufficient Balance")
    continue
 else:
    change = money_paid - total_cost
    break


print_receipt(order, total_cost, money_paid, change, discounted if is_senior else 0, vat, is_senior)



