# Week 2 Capstone: Shopping Cart System

# a list to keep both pieces of info together as tuple i.e., (name, price).
cart = []

# keeps running until the user types "done".
while True:
    # get name of item
    # remove unwanted spaces at the start and end with .strip() 
    # fix capitalization to proper case with .title()
    item_name = input("Enter item name (or 'done' to finish): ").strip().title()

    # "done" means stop signal, heance break out of the loop.
    if item_name.lower() == "done":
        break

    # get the price separately to pair it with the item.
    price = float(input(f"Enter price for {item_name}: "))

    # skip negative prices
    if price < 0:
        print("Price cannot be negative.")
        continue

    # keep each item's details together.
    cart.append((item_name, price))

# total is initially zero
total = 0.0

# display each item's details with index starting at 1
for index, (name, price) in enumerate(cart, start=1):
    print(f"{index}. {name:<10}{"₦"+f'{price:.2f}':>10}")
    total += price

# display the total cost of the cart.
print(f"Total: ₦{total:.2f}")

# decide the delivery fee based on thresholds.
# using if/elif/else ensures only one condition applies.
if total >= 10000:
    delivery_fee = 0
else:
    delivery_fee = 1000

# display whether the delivery is free or has a cost
print("Free delivery!" if delivery_fee == 0 else f"Delivery fee is ₦{delivery_fee:.2f}.")
