def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price * (1 - discount_percent / 100)
    return price

price = float(input("Enter Price: "))
discount_percent = float(input("Enter Discount %: "))

print("Final Price:", calculate_discount(price, discount_percent))
