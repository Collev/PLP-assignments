price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

if discount_percent >= 20:
    discount_amount = (discount_percent / 100) * price
    final_price = price - discount_amount

if discount_percent >= 20:
    print(f"Final price after discount is:{final_price:}")
else:
    print(f"No discount applied.Original price is: {price:}")


