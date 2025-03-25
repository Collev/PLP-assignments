def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if it's 20% or higher.
    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Final price after applying the discount (if applicable)
    """
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    return price

price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

print(f"The final price is: {final_price:.2f}")
