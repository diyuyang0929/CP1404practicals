total_price = 0
Item = int(input("Number of items: "))
while Item < 0:
    print("Invalid input")
    Item = int(input("Number of items: "))
for i in range(1, Item + 1):
    price = float(input("Price of item: "))
    total_price += price
if total_price >= 100:
    total_price = total_price * 0.9
print(f"Total price for {Item} items is ${total_price:.2f}")
