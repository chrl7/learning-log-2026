# OOP
class Car:
    def __init__(self, brand, color, speed=0):
        self.brand = brand
        self.color = color
        self.speed = speed

    def drive(self, speed_increment):
        self.speed += speed_increment
        print(f"{self.brand} is now traveling at {self.speed} km/h")

    def stop(self):
        self.speed = 0
        print(f"{self.brand} has stopped.")

my_car = Car("Toyota", "Silver")
my_car.drive(40)    
my_car.drive(20)     
my_car.stop()  



# inheritance and polymorphism
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(f"{self.name} sound {self.sound}!")

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, sound="Meong")  
        self.breed = breed  

    def info(self):
        print(f"{self.name} is a purebred cat {self.breed}")

cat1 = Cat("Kitty", "Persia")
cat1.make_sound()  
cat1.info()         



# Error Handling (try-except & custom exception).
class InsufficientBalance(Exception):
    pass

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientBalance(f"Balance {self.balance} is insufficient to withdraw {amount}")
        self.balance -= amount
        print(f"Successfully withdrew {amount}. Remaining balance: {self.balance}")

account = BankAccount("Chrl", 50000)

try:
    account.withdraw(100000)
except InsufficientBalance as e:
    print(f"Transaction failed: {e}")

print("The program continues running after the error is handled.")



# file I/O
import csv

# Writing using a dictionary
with open("books2.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["title", "author", "year"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow(
        {"title": "Atomic Habits", "author": "James Clear", "year": 2018}
    )

# Reading as a dictionary (nama file disamakan: books2.csv)
with open("books2.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["title"], "-", row["author"])





# ====================================------------------------ Exercise -------------------======================================
# Exercise 1 : Attributes: title, author, number_of_pages, and pages_read (default 0). The read(number) method → increments pages_read by the specified number, then prints the progress, for example: "You have read 50 of 300 pages." The info() method → prints the title and author in a neat format 
class Book :
    def __init__(self, title, author, number_of_pages, pages_read=0):
        self.title = title
        self.author = author
        self.number_of_pages = number_of_pages
        self.pages_read = pages_read
    
    def read(self, total) :
        self.pages_read += total
        
        if self.pages_read > self.number_of_pages :
            self.pages_read = self.number_of_pages
            
        print(f"You have read {self.pages_read} pages out of {self.number_of_pages} pages")
        
    def info(self):
        print("===== Book Information =====")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print("==========================")
        
book1 = Book("the psychology of money", "Morgan Housel", 238)

book1.info()

book1.read(20)
book1.read(10)



# Exercise 2 :
# 1) Create an Employee class with the attributes name and salary, and a describe() method that prints: "[name] earns [salary]"
# 2) Create a Manager class that inherits from Employee, and add a bonus attribute. Override the describe() method so that it prints: "[name] earns [salary] + [bonus]"
# 3) Create an Intern class that also inherits from `Employee`, but override the `describe()` method so that it prints: "[name] is an intern with a stipend of [salary]"
# 4) Create a list containing several objects (Employee, Manager, Intern), then loop through them and call `describe()` on all of them—demonstrate that polymorphism works.
class Employee :
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def describe(self) :
        print(f"{self.name} earns {self.salary}")

class Manager (Employee) :
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary) 
        self.bonus = bonus
    
    def describe(self):
        print(f"{self.name} earns {self.salary} + {self.bonus}")
        
class Intern (Employee) :
    def describe(self):
        print(f"{self.name} is an intern with a stipend of {self.salary}")
        
employees = [
    Employee("Ayu", 4000000), Manager("chrl", 8000000, 2000000), Intern("Bagas", 2000000)
]

print("=====--- List Employees ---=====")
for emp in employees :
    emp.describe()



# Exercise 3 :
# 1) Create a custom exception called 'AgeInvalid' (inheriting from 'Exception')
# 2) Create a function 'voter_list(name, age)': a)If age < 0 → raise 'InvalidAge("Age cannot be negative")'. b)If age < 17 → raise 'InvalidAge("Not old enough to vote (minimum age is 17)")`. 3) If valid → print "[name] has been successfully registered as a voter."
# 3) Call voter_list() for 3 different cases (negative age, age under 17, valid age) wrapped in a try-except block, and print an error message if it fails
class AgeInvalid(Exception) :
    pass

def voter_list(name,age):
    if age < 0 :
        raise AgeInvalid("Age cannot be negative")
    elif age < 17 :
        raise AgeInvalid("Not old enough to vote (minimum age is 17)")
    else :
        print(f"{name} has been successfully registered as a voter")
        

testing = [("Agus", -2), ("Bayu", 14), ("Chrl",20)]

for name, age in testing :
    try:
        voter_list(name, age)
    except AgeInvalid as e :
        print(f"Registration for {name} failed {e}")



# Exerecise 4 :
# 1) Write a file named "student.csv" containing the headers "name", "score" and 3 rows of student data (use the standard "csv.writer")
# Read the "student.csv" file again, then calculate the average score for all students (remember: the values in the CSV are strings, so you must convert them to "int()"" or "float()"first!)
# Print the average score

import csv

student_data = [
    ["name", "score"],
    ["Ajeng", 80],
    ["Bagas", 89],
    ["Citra", 98]
]

with open("student.csv", mode="w", newline="", encoding="utf-8") as file :
    writer = csv.writer(file)
    writer.writerows(student_data)
print("File student.csv successfully created!")

total_scores = 0
total_students = 0

with open("student.csv", mode="r", encoding="utf-8") as file :
    reader = csv.reader(file)
    header = next(reader)
    
    for row in reader:
        name=row[0]
        score = float(row[1])
        total_scores += score
        total_students += 1
    

if total_students > 0:
    average = total_scores/ total_students
    print(f"number of students : {total_students}")
    print(f"average student score : {average:.2f}")