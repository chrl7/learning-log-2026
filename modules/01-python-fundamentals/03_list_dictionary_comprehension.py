# List Comprehension

# The usual way (loop):
numbers = [1, 2, 3, 4, 5]
squares = []
for n in numbers:
    squares.append(n ** 2)
print(squares)  # [1, 4, 9, 16, 25]

# Comprehension (more concise):
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
print(squares)  # [1, 4, 9, 16, 25]

# Using a filter (if) statement:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = [n for n in numbers if n % 2 == 0]
print(even)  # [2, 4, 6, 8, 10]

# Using a combination of transformation and filtering:
words = ["apple", "orange", "mango", "kiwi"]
long_capitalized_words = [k.upper() for k in words if len(k) > 4]
print(long_capitalized_words)  # [‘APPLE’, ‘ORANGE’, ‘MANGO’]



# Dictionary Comprehension

# Standard method (loop):
names = ["Ani", "Budi", "Citra"]
name_lengths = {}
for n in names:
    name_lengths[n] = len(n)
print(name_lengths)  # {‘Ani’: 3, ‘Budi’: 4, ‘Citra’: 6}

# Using comprehension:
names = ["Ani", "Budi", "Citra"]
length_of_names = {n: len(n) for n in names}
print(length_of_names)  # {‘Ani’: 3, ‘Budi’: 4, ‘Citra’: 6}

# With a filter:
item_prices = {"apple": 5000, "orange": 3000, "mango": 8000}
expensive = {k: v for k, v in item_prices.items() if v > 4000}
print(expensive)  # {‘apple’: 5000, ‘mango’: 8000}




# ====================================------------------------ Exercise -------------------======================================
# Exercise 1 : Create a list of numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Use a list comprehension to create a new list containing the cube (third power) of each number.
numbers = [1,2,3,4,5,6,7,8,9,10]
cube = [n ** 3 for n in numbers]
print(cube)

# Exercise 2 : From the same list of numbers, use a list comprehension to create a new list containing only odd numbers greater than 3.
odd = [n for n in numbers if n % 2 == 1 and n > 3]
print(odd)

# Exercise 3 : Create a list of city_names = [“jakarta”, “bandung”, “surabaya”, ‘medan’, “wonosobo”]. Use a list comprehension to create a new list containing the city names with the first letter capitalized (use .capitalize() or .title()), but only for cities whose names are longer than 6 letters.
city_names = ["jakarta", "bandung","surabaya", "medan", "wonosobo"]
capital = [k.capitalize() for k in city_names if len(k) > 6]
print(capital)

# Exercise 4 : Create a dictionary comprehension from the list of numbers = [1, 2, 3, 4, 5], where the key is the number itself, and the value is “even” or “odd” (hint: you'll need a conditional expression—x if condition, else y—within the comprehension).
numbers = [1,2,3,4,5]
test = {k : "even" if k % 2 == 0 else "odd" for k in numbers}
print(test)

# Exercise 5 : Create a new dictionary comprehension that contains only students with grades ≥ 60 (passing), where the values are replaced with the following grades: “A” if ≥ 85, “B” if 70–84, and ‘C’ if 60–69. (This requires a nested conditional expression within the comprehension—a “difficult” level challenge!)
student_grades = {"Ani": 85, "Budi": 55, "Citra": 92, "Dedi": 40, "Eka": 78}
result = {name: "A" if value >= 85 else ("B" if value >= 70 else "C") for name, value in student_grades.items() if value >= 60}
print(result)