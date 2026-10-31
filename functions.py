# Exercise 1

#def calculate_tax(price, rate):
 #   return price * rate

#tax1 = calculate_tax(100, 0.07)
#tax2 = calculate_tax(250, 0.08)

#print(f"Tax on $100 at 7%: ${tax1:.2f}")
#print(f"Tax on $250 at 8%: ${tax2:.2f}")
#print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}")

#Exercise 2

#def apply_discount(price, tier):
 #   if tier == "Gold":
  #      return price * 0.85
   # elif tier == "Silver":
    #    return price * 0.90
    #elif tier == "Bronze":
    #    return price * 0.95
    #else:
    #    return price


#price = 200
#tiers = ["Gold", "Silver", "Bronze", "None"]

#for tier in tiers:
#    print(f"{tier}: ${apply_discount(price, tier):.2f}")


# Exercise 3

# write it out manually first, then refactor into a function

#discounted = apply_discount(200, "Gold")
#tax = calculate_tax(discounted, 0.07)
#after_tax = discounted + tax
#print(f"After gold discount: ${after_tax:.2f}")
#print(f"After Tax: ${after_tax:.2f}")

# Refactor into a function

#def final_price(price, tier, tax_rate):
 #   discounted = apply_discount(price, tier)
  #  tax = calculate_tax(discounted, tax_rate)
   # return discounted + tax


#print(f"Final price: ${final_price(200, 'Gold', 0.07):.2f}")


# Exercise 4

#orders = [(200, "Gold"), (150, "Silver"), (80, "Bronze"), (500, "None")]

#for price, tier in orders:
 #  total = final_price(price, tier, 0.07)
  # print(f"Price: ${price:.2f}, Tier: {tier}, Final Price: ${total:.2f}")


#exercise 5
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1




# Exercise 6

#x = 100 # apple # Global variable

#def double_it():
 #   x = 999 # another apple
  #  return x * 2

#	print(x)
#print(double_it())
#print(x)


