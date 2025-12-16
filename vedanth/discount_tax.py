def calculate_total(items):
    total = 0
    for price in items:
        total += price
    return total


def calculate_discount(total_amount, discount_rate):
    discount = total_amount * (discount_rate / 100)
    return discount


def calculate_tax(amount_after_discount, tax_rate):
    tax = amount_after_discount * (tax_rate / 100)
    return tax


def calculate_final_amount(total, discount, tax):
    final_amount = total - discount + tax
    return final_amount



items_cost = [int(x) for x in input("Please enter item cost seperated by ',' : ").split(",")]
discount_rate = 10  
tax_rate = 5        


total = calculate_total(items_cost)
print("Total:", total)

discount = calculate_discount(total, discount_rate)
print("Discount:", discount)

amount_after_discount = total - discount
print("Amount After Discount:", amount_after_discount)

tax = calculate_tax(amount_after_discount, tax_rate)
print("Tax:", tax)

final_amount = calculate_final_amount(total, discount, tax)
print("Final Amount:", final_amount)
