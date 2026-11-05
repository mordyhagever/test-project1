from validations import *
from orders_manager import *


def active1():
    return create_order()
def active2():
    return print_all_orders()
def active3():
    pass
def active4():
    pass
def active5():
    pass

def print_menu():
    print("""
    ======= ORDER MANAGER =======
    1. Create order
    2. Show all orders
    3. Find order by ID
    4. Close order
    5. Show sales report
    0. Exit
    """)
    choose = input()
    while not is_int(choose):
        choose = input("Enter a valid number: ")
        while not check_orders_menu(choose):
            choose = input("only a number from the menu: ")
    choose = int(choose)
    return choose

def activator():
    user_choice = print_menu()
    while user_choice != 0:
        if user_choice == 1:
            print(active1())
        elif user_choice == 2:
            print(active2())
        elif user_choice == 3:
            print(active3())
        elif user_choice == 4:
            print(active4())
        elif user_choice == 5:
            print(active5())
        user_choice = print_menu()
    return "The progress has been finished"

# print(activator())
