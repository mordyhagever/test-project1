from data_base_example import *

def str_to_int(number):
    try:
        return int(number)
    except ValueError:
        return "ERROR, can't convert to a number"

def is_id_legal(number):
    try:
        number = int(number)
        if number > 0:
            return True
    except ValueError:
        return False

def check_str(word):
    if len(word) == 0:
        return False
    return True

def check_orders_menu(number):
    try:
        number = int(number)
        if number < 1 or number > 2:
            return False
        return True
    except ValueError:
        return True


def is_product_id_exist(product_id):
    if product_id > 5 or product_id < 1:
            return False
    return True


def name_according_to_id(product_id):
    for item in products:
        if item["id"] == product_id:
            return item["name"]
    return "product is unavailable"

def menu_choose_checker(number):
    try:
        number = int(number)
        if number < 0 or number > 5:
            return False
        return True
    except ValueError:
        return False

def is_int(number):
    try:
        number = int(number)
        return True
    except ValueError:
        return False

