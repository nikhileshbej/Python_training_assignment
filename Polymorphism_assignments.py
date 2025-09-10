# Scenario:
 
# You are building the backend logic of a product and order management system for an e-commerce platform like Amazon or Flipkart. The system needs to handle products, users, payments, discounts, and different order behaviors dynamically.
 
# Q1. Product Search System (Static Polymorphism)
 
# Problem Statement:
# Implement a class ProductSearch that allows searching products with different combinations of criteria (name, category, price range).
 
# Requirements:
# Use default arguments and/or *args, **kwargs to simulate method overloading.
# Allow the following types of searches:
# Only by name
# Name and category
# Name, category, and price range

class ProductSearch:
    def search(self, name, category = None, price = None):
        if (category is not None and price is not None):
            print("Product is found based on the Name, Category and price range provided")
        elif (category is not None):
            print("Products is found based on the Name and Category")
        else:
            print("Product is found based on name only")

product = ProductSearch()
 
print("============= First assignment ==================")
product.search("Samsung TV")
product.search("Samsung TV", "24 inch")
product.search("Samsung TV", "20-incg", 15000)



# Q2. Cart System with Quantity Variations (Static Polymorphism)
 
# Problem Statement:
# Design a class Cart that can add multiple products with variable quantities using *args or **kwargs.
 
# Requirements:
# Add multiple products at once with name and quantity
# Simulate static polymorphism using variable arguments

class Product:
    def product_detais(self, **product_details):
        print("Product details ===================")
        for key, value in product_details.items():
            print(f"Product {key} is : {value}")


print("============= Second assignment ==================")
cart_item = Product()
cart_item.product_detais(name = "Samsung")
cart_item.product_detais(name = "Samsung", qauantity = 5)
cart_item.product_detais(name = "Samsung", qauantity = 5, price = 5000)


# Q3. Discount Application (Static Polymorphism)
 
# Problem Statement:
# Create a class Discount that allows applying different types of discounts:
 
# Flat discount
# Percentage discount
# Buy One Get One
 
# Use static polymorphism to overload the method using default parameters or *args

class Discount:
    def apply_discount(self, flat = None, percentage = None, BueOneGetOne = None):
        if (flat is not None and percentage is None and BueOneGetOne is None):
            print("Apply flat discout")
        elif (percentage is not None and BueOneGetOne is None):
            print("Apply percentahe discount")
        elif (BueOneGetOne is not None):
            print("Apply Buy One Get One dicount")
        else:
            print("No discount is applied")


discount = Discount()
print("============= Third assignment ==================")
discount.apply_discount("flat")
discount.apply_discount(None, "percentage")
discount.apply_discount(None, None, "BueOneGetOne")


# Q4. Payment System (Dynamic Polymorphism)
 
# Problem Statement:
# Implement a base class Payment and subclasses CreditCardPayment, UPIPayment, and CODPayment. Each should override a method pay().
 
# Requirements:
# Override pay() method in each class to simulate different payment methods

class Payment:
    def pay(self):
        print("Pay payment")

class CreditCardPayment(Payment):
    def pay(self):
        print("Make a credit card payment")

class UPIPayment(Payment):
    def pay(self):
        print("Make a UPI payment")

class CODPayment(Payment):
    def pay(self):
        print("Make a COD payment")


payment_mothods = [CreditCardPayment(), UPIPayment(), CODPayment()]

print("============= Fourth assignment ==================")
for item in payment_mothods:
    item.pay()

