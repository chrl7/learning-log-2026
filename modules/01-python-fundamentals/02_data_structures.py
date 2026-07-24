# List
fruits = ["apple", "orange", "mango"]
fruits.append("banana")       # add to the end
fruits.insert(1, "grape")     # insert at a specific position
fruits.remove("orange")       # remove by value
fruits.pop()                  # remove and return the last item

print(fruits)
print(len(fruits))            # number of items
print(sorted(fruits))         # sort (does not modify the original)
print("apple" in fruits)      # check for presence -> True/False


# Tuple
coordinates = (-7.3925, 109.9024)   # lat, long for Wonosobo
lat, long = coordinates             # unpacking

print(f"Lat: {lat}, Long: {long}")
# coordinates[0] = 10               <- this will cause an ERROR because tuples are immutable
print(coordinates.count(-7.3925))   # count the number of occurrences of a value


# Dictionary
students = {
    "name": "Chrl",
    "age": 20,
    "city": "Magelang"
}

print(students["name"])                 # access via key
students["major"] = "IT"                # add new key-value pair
students.update({"age": 21})            # update value
print(students.keys())                  # all keys
print(students.values())                # all values
print(students.items())                 # all key-value pairs
print(students.get("hobby", "none"))    # safe get; returns default if key doesn't exist


# Set
visited_cities = {"Jambi", "Jakarta", "Magelang", "Jakarta"}  # duplicates are automatically removed
print(visited_cities)  # {‘Jambi’, ‘Jakarta’, ‘Magelang’}

visited_cities.add("Yogyakarta")
visited_cities.discard("Jakarta")  # safe even if the item doesn't exist
print(visited_cities)

set_a = {1, 2, 3}
set_b = {2, 3, 4}
print(set_a & set_b)  # intersection -> {2, 3}
print(set_a | set_b)  # union -> {1, 2, 3, 4}
print(set_a - set_b)  # difference -> {1}



# ====================================------------------------ Exercise -------------------======================================

# Exercise 1 : Create a list test_scores = [80, 90, 75, 88, 95]. Add the score 70 at the end, then sort the list from smallest to largest (using a method, not sorted()). Print the result.
test_scores = [80, 90, 75, 88, 95]
test_scores.append(70)
test_scores.sort()
print(test_scores)


# Exercise 2 : Create a tuple tourist_location = (“Prambanan Temple”, “-7.7520”, “110.4914”). Unpack it into 3 variables: place_name, lat, and long. Print the results in full sentence format.
tourist_location = ("Prambanan Temple", -7.7520, 110.4914)
place_name, lat, long = tourist_location
print(f"The tourist is currently in {place_name} at coordinates lat: {lat}, long: {long}")


# Exercise 3 : Create a dictionary `product` = {“name”: “Laptop”, “price”: 8000000, “stock”: 5}. Add a new key ‘category’: “Electronics”, then decrease the stock by 2 (because it was sold), and then print the entire dictionary neatly (use a `for` loop over the keys and values in `produk.items()`).
product = {
    "name" : "Laptop",
    "price" : 8000000,
    "stock" : 5
}
product["category"] = "Electronic"
product["stock"] -= 2
for key, value in product.items():
    print(key, value)
    

# Exercise 4 : You have two sets: andi_hobbies = {“reading”, “gaming”, “coding”} and budi_hobbies = {“gaming”, ‘sports’, “coding”}. Find: (a) the hobbies that both of them share, (b) the hobbies that only Andi has, (c) the union of all hobbies without duplicates.
andi_hobbies = {"reading", "gaming", "coding"}
budi_hobbies = {"gaming", "sports", "coding"}
print(andi_hobbies & budi_hobbies)  
print(andi_hobbies - budi_hobbies)  
print(andi_hobbies | budi_hobbies)  


# Exercise 5 : Find the student with the highest score without using the `max()` function directly on the dictionary—use a `for` loop to compare them one by one. Print only the student's name.
students_list = [
    {"name": "Ani", "score": 85},
    {"name": "Budi", "score": 70},
    {"name": "Citra", "score": 92}
]

highest = students_list[0]
for stdn in students_list:
    if stdn["score"] > highest["score"] :
        highest = stdn
        
print(highest["name"])