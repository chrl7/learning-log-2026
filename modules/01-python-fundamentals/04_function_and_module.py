# Anatomy Function
def calculate_discount(price, discount_percentage):
    """Calculates the price after the discount."""
    discount = price * (discount_percentage / 100)
    final_price = price - discount
    return final_price

# Calling the function
shirt_price = calculate_discount(200000, 10)
print(f"Price after discount: Rp{shirt_price:,.0f}")



# parameter vs argument
def sayHello(name):      # "name" here is a PARAMETER (definition)
    return f"Hello, {name}!"

result = sayHello("Bayu")  # "Bayu" here is an ARGUMENT (the actual value passed)
print(result)



# Return value 
def no_return(x):
    print(x * 2)   # just prints, doesn't return anything

def with_return(x):
    return x * 2   # can be stored in a variable

a = no_return(5)   # a = None
b = with_return(5)  # b = 10



# Default Argument
def create_account(username, role="member"):
    return f"Account {username} created with role: {role}"

print(create_account("aji"))            # role uses the default "member"
print(create_account("admin1", "admin")) # role is overridden to "admin"



# *args
def total_spending(*price):
    print(type(price))  # <class "tuple">
    return sum(price)

print(total_spending(10000, 25000, 5000))       # 40000
print(total_spending(10000, 25000, 5000, 7000)) # 47000 - any number of items!



# **kwargs
def create_profile(**info):
    print(type(info))       # <class "dict">
    for key, value in info.items():
        print(f"{key}: {value}")

create_profile(name="Chrl", age=20, city="Magelang")



# All of Them Combined
def create_report(title, *author, year=2026, **metadata):
    print(f"Title: {title}")
    print(f"Author: {author}")
    print(f"Year: {year}")
    print(f"Metadata: {metadata}")

create_report("Data Analysis", "Chrl", "Bayu", year=2025, category="research")



# Local variable
def calculate_area(length, width):
    area = length * width  # "area" is a LOCAL variable
    return area

result = calculate_area(5, 3)
print(result)  # 15 - this is fine, because "result" holds the return value

# print(area)  # ERROR! NameError: name ‘area’ is not defined



# Global variable
store_name = "Chrl Store"  # GLOBAL variable

def display_header():
    print(f"Welcome to {store_name}")  # can READ the global variable

display_header()  


# Import module

import math
import random

print(math.sqrt(16))         
print(random.randint(1, 10))  




# ====================================------------------------ Exercise -------------------======================================

# Exercise 1 : Create a function called `check_graduation(score)` that: 1. Takes a single parameter `score` (a number between 0 and 100). 2. Returns "Passed" if `nilai` is greater than or equal to 60; otherwise, returns "Failed". 3. Test it with at least 3 different values and print the results
def check_graduation(score):
    if score < 0 or score > 100:
        return "Enter a score between 0 and 100"
    elif score >= 60:
        return "Passed"
    else:
        return "Failed"

result1 = check_graduation(20)
result2 = check_graduation(75)
result3 = check_graduation(150)

print(result1)  
print(result2)  
print(result3)  



# Exercise 2 : Create a function "create_profile(name, *hobbies, city="Unknown", **contact" that: name = required parameter, *hobbies = accepts multiple hobbies (any number), city → default argument, **contact → accepts optional contact information (e.g., email="...", phone_number="..."), Return a complete bio string that combines all of the above information (you may use multi-line f-strings)
def create_profile(name, *hobbies, city="Unknown", **contact):
    hobbies_str = ", ".join(hobbies) if hobbies else "none"
    contact_str = ", ".join(f"{k}: {v}" for k, v in contact.items()) if contact else "none"
    
    biodata = f"""=====--- {name} profile ---=====
    City     : {city}
    Hobbies  : {hobbies_str}
    Contact  : {contact_str}"""
    
    return biodata

profile = create_profile("chrl", "martial arts", "listening to podcast", city="Yogyakarta", email="test@gmail.com", phone_number=123456)

print(profile)



# Exercise 3 : Declare a global variable "stock_items" = 50. Create a function "decrease_stock(current_stock, quantity_sold)" that returns the new stock (use the return statement, NOT a global variable). Call that function twice in a row (sell 10 items, then sell 15 more items), updating `stock_items` each time. Print the final stock
stock_items = 50
def decrease_stock (current_stock, quantity_sold) :
    new_stock = current_stock - quantity_sold
    return new_stock

stock_items = decrease_stock(stock_items, 10)
stock_items = decrease_stock(stock_items, 15)
    
print("final stock:", stock_items)
    

