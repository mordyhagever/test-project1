import json
from validations import *
from data_base_example import *

def get_all_orders():
    with open("orders.json", "r") as file:
        return json.load(file)

def add_to_json(order):
    all_orders = get_all_orders()
    all_orders.append(order)
    with open("orders.json", "w") as file:
        json.dump(all_orders, file, indent=2)
    return "File has been updated"

def update_json(order_id, update_parameter, update):
    all_orders = get_all_orders()
    for order in all_orders:
        if order["id"] == order_id:
            order[update_parameter] = update
    with open("orders.json", "w") as file:
        json.dump(all_orders, file, indent=2)
    return "File has been updated"



def search_by_id():
    order_id = input("Enter order id: ")
    while not is_id_legal(order_id):
        order_id = input("Enter a valid number id: ")
    order_id = int(order_id)
    loaded = get_all_orders()
    for order in loaded:
        if order["id"] == order_id:
            return order
    return "Order has not found"



