
# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}
# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
# Order list to store the items ordered by the customer
order_list = []

# Function to print the menu based on the category
def print_menu(category):
    i = 1
    menu_items = {}
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")
    for key, value in category.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                item_name = f"{key} - {sub_key}"
                item_price = sub_value
                print(f"{i}      | {item_name.ljust(26)} | ${item_price}")
                menu_items[i] = {"item": item_name, "price": item_price}
                i += 1
        else:
            item_name = key
            item_price = value
            print(f"{i}      | {item_name.ljust(26)} | ${item_price}")
            menu_items[i] = {"item": item_name, "price": item_price}
            i += 1
    return menu_items

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")
# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    print("Please select a category:")
    print("1: Snacks\n2: Meals\n3: Drinks\n4: Dessert")
    # Get the customer's input
    category_input = input("Type menu number: ")
    # Check if the customer's input is a number
    if category_input.isdigit():
        category_input = int(category_input)
        if category_input in range(1, 5):
            category_name = list(menu.keys())[category_input - 1]
            print(f"You selected {category_name}")
            menu_items = print_menu(menu[category_name])
            # 2. Ask customer to input menu item number
            item_input = input("Type menu item number: ")
            # 3. Check if the customer typed a number

            # Convert the menu selection to an integer
            if item_input.isdigit():
                item_input = int(item_input)
                
                # 4. Check if the menu selection is in the menu items
                # Store the item name as a variable

                if item_input in menu_items:
                    item_name = menu_items[item_input]['item']
                    item_price = menu_items[item_input]['price']
                    
                    # Ask the customer for the quantity of the menu item
                    # Check if the quantity is a number, default to 1 if not
                    quantity_input = input(f"How many of {item_name} do you want? ")
                    if quantity_input.isdigit():
                        quantity_input = int(quantity_input)
                    # Add the item name, price, and quantity to the order list
                    # Tell the customer that their input isn't valid
                    # Tell the customer they didn't select a menu option
                    else:
                        quantity_input = 1
                        print("Invalid quantity. Defaulting to 1.")

                    order_list.append({
                        "item": item_name,
                        "price": item_price,
                        "quantity": quantity_input
                    })
                    # 5. Check the customer's input
                    # Keep ordering
                    # Exit the keep ordering question loop
                    # Complete the order
                    # Since the customer decided to stop ordering, thank them for
                    # their order
                    # Exit the keep ordering question loop

                    # Tell the customer to try again
                    keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").strip().upper()
                    if keep_ordering == 'N':
                        place_order = False
                else:
                    print("Invalid item number selected.")
            else:
                print("Invalid input. Please enter a valid item number.")
        else:
            print("Invalid category number selected.")
    else:
        print("Invalid input. Please enter a valid category number.")

# Print the customer's order summary
print("\nThis is what we are preparing for you:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|---------")

total_cost = 0
for order in order_list:
    item_name = order["item"]
    item_price = order["price"]
    item_quantity = order["quantity"]
    print(f"{item_name.ljust(26)} | ${str(item_price).ljust(6)} | {str(item_quantity).ljust(7)}")
    total_cost += item_price * item_quantity

print("\nTotal cost of your order: ${:.2f}".format(total_cost))
