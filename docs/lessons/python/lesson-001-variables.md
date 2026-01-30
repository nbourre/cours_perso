---
title: "Introduction to Variables"
description: "Learn how to create and use variables to store and manipulate data in Python"
difficulty: "Beginner"
duration: "30 minutes"
tags: [python, variables, data-types, basics]
learning_objectives:
  - "Understand what variables are and why they're useful"
  - "Create and assign values to variables"
  - "Understand Python data types (strings, integers, floats, booleans)"
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# Introduction to Variables

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what variables are and why they're useful
- Create and assign values to variables
- Understand Python data types (strings, integers, floats, booleans)

## Introduction

In programming, a **variable** is a named container that stores a value. Think of it like a labeled box where you can put information that your program uses and refers to later.

Variables are essential because they allow you to:
- **Store data** that your program needs to work with
- **Reference data** by a meaningful name instead of memorizing values
- **Change values** as your program runs
- **Reuse data** throughout your code

Without variables, programming would be nearly impossible!

## What Is a Variable?

A variable has three key parts:
1. **Name**: How you refer to the variable (e.g., `age`, `user_name`)
2. **Type**: What kind of data it stores (e.g., text, number)
3. **Value**: The actual data stored (e.g., 25, "Alice")

### Creating a Variable

In Python, creating a variable is simple:

```python
variable_name = value
```

**Example**:
```python
age = 25
name = "Alice"
height = 5.6
is_student = True
```

The `=` sign is called the **assignment operator**. It means "store this value in this variable."

## Python Data Types

Python has several basic data types. Let's explore the most common ones:

### 1. Integer (int)
Whole numbers without decimals.

```python
age = 25
temperature = -5
count = 0
```

### 2. Float (float)
Numbers with decimals.

```python
price = 19.99
pi = 3.14159
height = 5.6
```

### 3. String (str)
Text, enclosed in quotes (single `'` or double `"`).

```python
name = "Alice"
greeting = 'Hello, World!'
address = "123 Main Street"
```

### 4. Boolean (bool)
True or False values (used for logic and decisions).

```python
is_student = True
is_online = False
has_license = True
```

## Naming Variables

When you name a variable, follow these conventions:
- ✅ **Use lowercase letters**: `user_name`
- ✅ **Use underscores between words**: `first_name`, `is_online`
- ✅ **Use meaningful names**: `age` instead of `a`
- ❌ **Avoid spaces**: `user name` doesn't work
- ❌ **Don't start with numbers**: `2cars` is invalid, but `cars2` is okay
- ❌ **Don't use Python keywords**: `class`, `def`, `for` are reserved

**Good variable names**:
```python
user_age = 25
total_price = 99.99
is_active = True
customer_name = "John"
```

**Avoid these**:
```python
a = 25                  # Not meaningful
User_Age = 25          # Use lowercase
user age = 25          # Can't use spaces
2user = 25             # Can't start with number
```

## Exercises

### Exercise 1: Create Your First Variables
Create variables to store information about yourself.

**Task**: Write a Python program that creates these variables:
- Your name (string)
- Your age (integer)
- Your height in meters (float)
- Whether you like coding (boolean)

**Example Solution**:
```python
name = "Alice"
age = 25
height = 1.75
likes_coding = True

print(name)          # Output: Alice
print(age)           # Output: 25
print(height)        # Output: 1.75
print(likes_coding)  # Output: True
```

### Exercise 2: Store Information About a Product
Create variables to represent a product in an online store.

**Task**: Create variables for:
- Product name (string)
- Price (float)
- Quantity in stock (integer)
- On sale (boolean)

**Example Solution**:
```python
product_name = "Python Book"
price = 29.99
quantity_in_stock = 150
on_sale = True

print(f"{product_name}: ${price}")
```

## Assessment

### Self-Check Questions

1. **What is a variable and why do we use them?**
   - A variable is a named container that stores data. We use variables to store information our program needs, make code more readable, and make values easy to change.

2. **How do you create a variable in Python?**
   - Use the syntax: `variable_name = value`. For example, `age = 25`.

3. **What are the four basic data types mentioned in this lesson?**
   - Integers (whole numbers), Floats (decimals), Strings (text), and Booleans (True/False).

4. **Can you name a variable with a space in it? Why or why not?**
   - No, Python doesn't allow spaces in variable names. Use underscores instead: `user_name` not `user name`.

5. **Write a Python line that creates a variable called `favorite_color` with the value "blue".**
   - `favorite_color = "blue"`

## Summary

Variables are fundamental to programming. They let you store, reference, and manipulate data. Remember:

- Create variables with: `name = value`
- Use meaningful, lowercase names with underscores
- Python has four basic types: int, float, str, bool
- Once created, you can use variables throughout your code

In the next lesson, you'll learn how to do things with variables—calculating with numbers, combining strings, and making decisions based on their values.

## Next Steps

- Practice creating variables with different data types
- Experiment with printing variables
- Look at the [Functions lesson](lesson-002-functions.md) to learn how to organize code with variables
- Explore more Python data types (lists, dictionaries) in future lessons

---

*Ready to learn more? Check out [Functions: Code Reuse and Organization](lesson-002-functions.md).*
