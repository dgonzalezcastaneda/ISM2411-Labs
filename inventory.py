# what is most supprising to me about list is how the list has a certain order. Numbers go be for letters and special characters go befor numbers, it its very instresting to me.
# In python, you can use commands to find a certain item in a list, where in excel you would have to look for it manually. In a buisness setting it could be very useful to save time. 



#inventory.py
#author: [Diego Gonzalez]
#Module 10 lab: Inventory list manager

print("--- Exercise 1: Build the list ---")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("--- Exercise 2: index practice ---")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle]) 



print("--- Exercise 3: slicing practice ---")
print(inventory[:3]) 
print(inventory[-2:])
print(inventory[::2])


print("--- Exercise 4: Modifying the list ---")
inventory.append("envelope")
print(inventory) # output: ['pen', 'notebook', 'stapler', 'tape', 'marker', 'envelope']
inventory.remove("tape")
print(inventory) # output: ['pen', 'notebook', 'stapler', 'marker', 'envelope']
inventory.sort()
print(inventory) # output: ['envelope', 'marker', 'notebook', 'pen', 'stapler']

print("--- Exercise 5: Tuple comparison ---")
coords = (40.7128, -784.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect cordinates: a location should never change by accident.")

print(coords)


print("--- Exercise 6: Average list of sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")


print("--- Exercise 7: Accumulator pattern ---")

prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discount = []
for price in prices:
    discount.append(round(price * .9, 2))

print("Original prices:", prices)
print("Discounts:", discount)

print("--- Exercise 8: Filter above a threshold ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print("High sales:", high_sales)
print("Number of high sales:", len(high_sales))
print("Average of high sales:", sum(high_sales) / len(high_sales))






