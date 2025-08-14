def calculate_discount(price, discount_percent):
    # Check if discount is 20% or more
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Example usage
print(calculate_discount(1000, 25))  # 750.0 (discount applied)
print(calculate_discount(1000, 10))  # 1000 (no discount)
