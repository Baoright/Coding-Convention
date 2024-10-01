 def calculate_sum(first_number, second_number):
    # Tính tổng của hai số
    total_sum = first_number + second_number
    return total_sum

def calculate_total_price(item_list):
    total_price = 0
    for item in item_list:
        total_price += item.price
    return total_price

