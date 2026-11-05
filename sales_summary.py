from json_handler import get_all_orders

def show_sales_summary():
    all_sales = get_all_orders()
    sum_orders = len(all_sales)
    sum_money_closed_order = 0
    highest_paid_order = max(all_sales, key=lambda p: p["total (after discount)"])
    top_three_orders = list(sorted(all_sales, key=lambda p: p["total (after discount)"], reverse=True))
    for order in all_sales:
        if order["status"] == "CLOSED":
            sum_money_closed_order += order["total (after discount)"]
    top_three_id = []
    for order in top_three_orders:
        top_three_id.append(order["id"])
    highest_paid_order = highest_paid_order["id"]
    return {
        "sum_orders": sum_orders,
        "sum sales from closed order": sum_money_closed_order,
        "highest paid order" : highest_paid_order,
        "top three orders": top_three_id,
    }



