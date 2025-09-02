
# Create a tuple named product containing the following items: "Laptop", 50000, Black ,'Samsung' and "Electronics". Print the tuple.
product = ("Laptop", 50000, "Black", 'Samsung', "Electronics")
print(product)

# Access and print the second element of the tuple product
print("The second element is: ", product[1])

# Slice and print the last two elements of the product tuple.
sliced_tuple = product[-2: len(product)]
print("Sliced tuple = ", sliced_tuple)

# Check whether "Electronics" is present in the product tuple and print a message.
if "Electronics" in product:
    print("Electronics is present")
else:
    print("Electronics is not present")


# Create a tuple of 5 product prices: (1000, 1500, 1200, 1100, 900). Count how many times 1000 appears.
product_price =  (1000, 1500, 1200, 1100, 900)
print("Occurance of 1000 is ", product_price.count(1000))

# Find and print the maximum and minimum price from the prices tuple.
print("Max price = ", max(product_price))
print("Min price =", min(product_price))

# Use a loop to print each item from the product tuple on a new line.
print("\nItem from the product tuple are :")
for item in product:
    print(item)

# Convert the product tuple to a list. Change the price to 55000, then convert it back to a tuple. Print the updated tuple.
product_list = list(product)
product_list[1] = 55000
product = tuple(product_list)
print(product_list)

#Add a new item "In Stock" to the product tuple (simulate adding by concatenation).
in_stock = ("In Stock",)
product = product + in_stock
print(product)

#Remove "Electronics" from the product tuple (by converting to list, removing, and converting back).
product_list = list(product)
product_list.remove("Electronics")
product = tuple(product_list)
print(product)
 
#Unpack the tuple product into three variables and print each variable.
name, price, color, *rest = product
print("name = ", name, " price = ", price, " color = ", color)

 
#Create a nested tuple that contains three product tuples inside it. Access and print the name of the second product in the nested tuple.
nested_tuple = (("Laptop", 50000, "Black"),
                ("Tablet", 10000, "Silver"),
                ("Desktop", 30000, "Blue"))
print("Name of seconds product =", nested_tuple[1][0])

