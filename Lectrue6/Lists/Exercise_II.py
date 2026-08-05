inventory = [
    ["Apple" , 50, 0.75],
    ["Banana", 100, 0.50],
    ["Orange", 75, 0.80]
]

def update_inventory(inv, item_name, quantity_sold):
    for item in inv:
        if item[0] ==  item_name:
            item[1] -= quantity_sold

def calculate_total_value(inv):
    return sum(item[1] * item[2] for item in inv)

def find_most_expensive(inv):
    return max(inv, key=lambda item: item[2])[0]

def add_item(inv, item_name, quantity, price):
    for item in inv:
        if item[0] == item_name:
            item[1] = quantity
            item[2] = price
            return
    inv.append([item_name, quantity, price])

update_inventory(inventory, "Banana", 20)

print("Total Value: ", calculate_total_value(inventory))
print("Most Expensive: ", find_most_expensive(inventory))
add_item(inventory, "Egg", 30, 0.25)
add_item(inventory, "Egg", 50,0.30)

