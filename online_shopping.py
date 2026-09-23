products = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 1500,
    "Keyboard": 800,
    "Mouse": 500
}

cart = {}

print("===== ONLINE SHOPPING =====")

while True:
    print("\nAvailable Products:")

    for product, price in products.items():
        print(product, "- ₹", price)

    product = input("\nEnter product name (or type 'exit'): ")

    if product.lower() == "exit":
        break

    if product not in products:
        print("Product not available.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Please enter a valid quantity.")
        continue

    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity

    print(quantity, product, "added to cart.")

print("\n===== YOUR CART =====")

total = 0

for product, quantity in cart.items():
    price = products[product]
    amount = price * quantity

    print(product)
    print("Price: ₹", price)
    print("Quantity:", quantity)
    print("Amount: ₹", amount)
    print("--------------------")

    total += amount

print("Total Amount: ₹", total)
print("Thank you for shopping!")