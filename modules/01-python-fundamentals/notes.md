# Variabel

Variable are like labeled boxes in a warehouse. You put a label on the box (for example, “age”), then put an item inside it (for example, the number 25). You can change the contents at any time without changing the label.

---

# dynamically typed

Python is dynamically typed—which means you don’t need to specify “this is a box specifically for numbers” at the beginning. Python automatically infers the data type from the contents.

---

# Basic data types in Python:

| type           | example    |
| :------------- | :--------- |
| int (integer)  | 25         |
| float          | 25.5       |
| str (string)   | "chrl"     |
| bool (boolean) | True/False |

---

---

# data structures

1. List []  
   -Bookshelf — items can be added, removed, and sorted; has an order
   -Mutable (can be changed), ordered, duplicates allowed
2. Tuple ()
   -GPS coordinates (lat, long) — once defined, cannot be changed
   -Immutable (cannot be changed), ordered
3. Dictionary {}
   -Dictionary/phone book — look up data using a “key,” not by order
   -Mutable, key-value pairs, unique keys
4. Set {} (without :)
   -Bag of unique marbles — order doesn’t matter, no duplicates allowed
   -Mutable, unordered, no duplicates

---

---

# List Comprehension & Dictionary Comprehension

## Quick Concept + Analogy

Imagine the traditional way (using a loop) is like writing a long letter asking someone to add items one by one to a basket. A comprehension is like giving a one-line instruction: “Collect all items that meet this condition and put them directly into the basket.”

General List Comprehension Pattern:
[expression for item in iterable if condition]

General Pattern for Dictionary Comprehension:
{key_expr: value_expr for item in iterable if condition}

The `if condition` part is optional—it’s only used if you want to filter.

Important note: Comprehensions are great for simple cases. When the logic gets complicated (many branching conditions, many lines of code), it’s better to use a regular loop. Comprehensions that are too complex actually make the code hard to read—remember the principle that "readability counts."

---

---

# Function and module

## Why Do We Need Functions?

Imagine writing code to calculate a discount on an item’s price, and need to use it repeatedly in many places. Without functions, have to copy and paste the same code over and over again. If there’s a bug or you need to make a change, you’d have to fix it in all those places. It’s tedious and prone to errors.
A function is a named block of code that can be called again at any time, with different inputs. The principle is: DRY (Don’t Repeat Yourself).

# \*args, and \*\*kwargs

*args : Accepts Multiple Unnamed Arguments. If don't know how many arguments will be passed, use *args. This collects all positional arguments into a tuple.

\**kwargs : Accepts Multiple Named (Keyword) Arguments. Similar to *args, but for arguments passed in the key=value format. It collects them into a dictionary.

The parameter order is mandatory: regular_param, \*args, default_param, \*\*kwargs

# local variable and global variabel

Local variable is Variables created within a function exist only for the duration of that function and can be accessed only from within the function itself.

Global variable is Variables declared outside a function (at the top-level of the program) can be accessed from anywhere, including from within a function.

# Module

A module is a .py file containing a collection of functions (or variables, classes) that can be reused in other files. It offers a level of "reusability" one step above that of a function—while a function is reusable within a single file, a module is reusable across files and projects.

---

---

# OOP

| term     | analogy                                          |
| :------- | :----------------------------------------------- |
| class    | Template/design                                  |
| object   | The actual result of the template                |
| atribut  | Characteristics/data (color, brand)              |
| method   | Capabilities/actions (go, stop)                  |
| **init** | The initial process when a new object is created |
| self     | “My own” — refers to the object itself           |
