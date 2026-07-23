# Variables and data types
name = "Chrl"      # str
age = 20           # int
height = 172.5     # float
employed = False   # bool
job = None         # NoneType, no value yet

# Check data types using the type() function
print(type(name))     # <class ‘str’>
print(type(age))      # <class ‘int’>
print(type(height))   # <class ‘float’>

# Python supports "type casting" (converting types)
age_str = str(age)              # convert int to str
print(age_str, type(age_str))

# f-strings, a modern way to combine text and variables
print(f"My name is {name}, I am {age} years old")



# ====================================------------------------ Exercise -------------------======================================

# Exercise 1 : Create 4 variables: city_name, population, area (in km², decimal), and provincial_capital (True/False). Print all their data types using type().
city_name = "wonosobo"
population = 920000
area = 33.00
provincial_capital = False
print(type(city_name))
print(type(population))
print(type(area))
print(type(provincial_capital))

# Exercise 2 : Create a variable `price = “50000”` (this is a string, not a number!). Convert it to an `int`, then calculate the total price for purchasing 3 items. Print the result using an f-string.
price = "5000"
price_int = int(price)
total_price = price_int * 3
print(f"The total price is {total_price}") 

# Exercise 3 : Declare a variable `celcius` with a value of 30. Convert it to Fahrenheit using the formula F = C * 9/5 + 32. Print the result in the following format: “A temperature of 30°C is equivalent to XX.X°F” (make sure the result is a float, not an int).
celcius = 30
far = celcius * 9/5 + 32
print(f"A temperature of 30°C is equivalent to {far}°F")

# Exercise 4 : There is a variable data = “Chrl,20,java” (a single string containing a name, age, and city separated by commas). Split it into 3 separate variables (name, age, city) using the `string.split(“,”)` method, then print each one along with its data type. (Hint: The results of the split are all strings—note that age needs to be converted to an int if you want to perform calculations later.)
data = "Chrl,20,java"
nama, umur, kota = data.split(",")
print(nama, type(nama))   # Chrl <class 'str'>
print(umur, type(umur))   # 25 <class 'str'>  <- perhatikan ini!
print(kota, type(kota))   # Jambi <class 'str'>

# Exercise 5 :  What are the results of `print(type(10 / 2))` versus `print(type(10 // 2))`? Explain why they differ (if they do), and then prove it by running the code.
print(type(10/2))
print(type(10//2))
answer = "In exercise number 5, the data types are different because 10/2 is a decimal division, whereas 10//2 is an integer division."