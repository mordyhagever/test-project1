from email.errors import CloseBoundaryNotFoundDefect

import data_base_example
from validations import *
from data_base_example import *
from json_handler import *
import json

def get_id():
    all_orders = get_all_orders()
    if not all_orders:
        return 1
    last_order = all_orders[-1]
    return last_order["id"] + 1

def price_after_discount(total):
    discount = 0
    if total < 300:
        return total, discount
    elif 700 > total >= 300:
        discount = 5
        return total - total * 0.05, discount
    elif 1500 > total >= 700:
        discount = 10
        return total - total * 0.1, discount
    else:
        discount = 15
        return total - total * 0.15, discount

def get_one_order():
    product_id = input("Enter product id: ")
    while not is_id_legal(product_id):
        product_id = input("Enter a valid number id: ")
    while not is_product_id_exist(int(product_id)):
        product_id = input("Product doesn't exist: ")
        while not is_id_legal(product_id):
            product_id = input("Enter a valid number id: ")
    product_id = int(product_id)
    quantity = input("Enter amount of product: ")
    while not is_id_legal(quantity):
        quantity = input("Enter a valid number of product: ")
    quantity = int(quantity)
    # while not is_there_enough_product(product_id, quantity):
    #     quantity = input("Not enough in stock, enter a lower amount: ")
    #     quantity = str_to_int(quantity)
    return (product_id, quantity)



def print_menu():
    print("""
    Enter your choice:
    1. Add another product to cart
    2. finish order and checkout
    """)
    choose = input()
    while not check_orders_menu(choose):
        choose = input("Enter a legal number: ")
    choose = str_to_int(choose)
    return choose

def create_order():
    total = 0
    order = {}
    order["items"] = []
    choose = print_menu()
    while choose != 2:
        order_id = get_id()
        order["id"] = order_id
        new_order = get_one_order()
        order["items"].append({"product_id": new_order[0], "quantity": new_order[1]})
        order["status"] = "OPEN"
        for item in products:
            if item["id"] == new_order[0]:
                total += item["price"] * new_order[1]
        choose = print_menu()
    print(f"price before discount: {total}")
    print(f"discount available: {price_after_discount(total)[1]}%")
    print(f"final price: {price_after_discount(total)[0]}")
    order["total (after discount)"] = price_after_discount(total)[0]
    add_to_json(order)

    return "order has been updated successfully"

def close_status():
    order_id = input("Enter order id: ")
    while not is_id_legal(order_id):
        order_id = input("Enter a valid number id: ")
    order_id = int(order_id)
    update_json(order_id, "status", "CLOSED")
    return "updated"


# print(create_order())






