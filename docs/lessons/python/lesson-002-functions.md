---
title: "Functions: Code Reuse and Organization"
description: "Learn to write reusable functions to organize your code and avoid repetition"
difficulty: "Beginner"
duration: "45 minutes"
tags: [python, functions, code-organization, parameters, return-values]
learning_objectives:
  - "Understand what functions are and why they're useful"
  - "Define and call functions with parameters"
  - "Use return values to get results from functions"
  - "Apply functions to organize code effectively"
prerequisites: [lesson-001-variables]
created: 2026-01-30
author: "LLM Assistant"
status: "published"
---

# Functions: Code Reuse and Organization

**Difficulty**: 🟢 Beginner | **Duration**: 45 minutes

**Tags**: [`python`](../../guides/tags-reference.md#python) · [`functions`](../../guides/tags-reference.md#functions) · [`code-organization`](../../guides/tags-reference.md#code-organization) · [`parameters`](../../guides/tags-reference.md#parameters) · [`return-values`](../../guides/tags-reference.md#return-values)

---

## Learning Objectives

By the end of this lesson, you will be able to:
- Understand what functions are and why they're useful
- Define and call functions with parameters
- Use return values to get results from functions
- Apply functions to organize code effectively

## Introduction

A **function** is a reusable block of code that performs a specific task. Functions are one of the most powerful tools in programming because they let you:

- **Avoid repetition**: Write code once, use it many times
- **Organize code**: Break complex problems into smaller pieces
- **Make code readable**: Give meaningful names to chunks of logic
- **Test more easily**: Test individual functions in isolation
- **Collaborate**: Work with teammates using shared functions

Without functions, your code would become long, confusing, and hard to maintain.

## What Is a Function?

A function has these parts:

1. **Name**: How you call the function
2. **Parameters** (optional): Inputs the function receives
3. **Body**: The code the function runs
4. **Return value** (optional): Output the function gives back

### Simple Function Structure

```python
def function_name(parameters):
    # Code goes here (the "body")
    return result
```

The `def` keyword means "define a function."

## Creating and Calling Functions

### Example 1: A Simple Function

```python
def greet():
    print("Hello, World!")

# Call the function
greet()  # Output: Hello, World!
greet()  # Output: Hello, World!
```

Notice we wrote `print("Hello, World!")` once in the function definition, but we can call it multiple times!

### Example 2: Functions with Parameters

Parameters let you pass data into a function. They're like inputs.

```python
def greet(name):
    print(f"Hello, {name}!")

# Call the function with different inputs
greet("Alice")   # Output: Hello, Alice!
greet("Bob")     # Output: Hello, Bob!
```

### Example 3: Functions with Return Values

A return value is what the function sends back to you.

```python
def add(a, b):
    result = a + b
    return result

# Call the function and use the result
sum1 = add(5, 3)      # sum1 is 8
sum2 = add(10, 20)    # sum2 is 30
print(sum1 + sum2)    # Output: 58
```

### Example 4: Complete Function

```python
def calculate_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Use the function
room_area = calculate_area(5, 4)  # 20 square meters
print(f"Room area: {room_area} m²")  # Output: Room area: 20 m²
```

## Function Parameters

### Single Parameter

```python
def square(number):
    result = number * number
    return result

print(square(5))  # Output: 25
```

### Multiple Parameters

```python
def add(a, b):
    return a + b

print(add(3, 7))  # Output: 10
```

### Default Parameters

You can provide default values:

```python
def greet(name="Friend"):
    return f"Hello, {name}!"

print(greet())           # Output: Hello, Friend!
print(greet("Alice"))    # Output: Hello, Alice!
```

## Return Values

Functions can return data that you use in your program:

```python
def get_user_info():
    age = 25
    name = "Alice"
    return name, age  # Can return multiple values!

name, age = get_user_info()
print(f"{name} is {age} years old")  # Output: Alice is 25 years old
```

## Exercises

### Exercise 1: Create a Simple Function
Create a function that converts Celsius to Fahrenheit.

**Formula**: `F = (C × 9/5) + 32`

**Task**: Write a function named `celsius_to_fahrenheit` that:
- Takes a Celsius temperature as a parameter
- Calculates the Fahrenheit equivalent
- Returns the result

**Example Solution**:
```python
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Test it
print(celsius_to_fahrenheit(0))    # Output: 32.0
print(celsius_to_fahrenheit(100))  # Output: 212.0
```

### Exercise 2: Function with Multiple Parameters
Create a function that calculates a discount price.

**Task**: Write a function named `apply_discount` that:
- Takes original price and discount percentage as parameters
- Calculates the new price
- Returns the discounted price

**Example Solution**:
```python
def apply_discount(original_price, discount_percent):
    discount_amount = original_price * (discount_percent / 100)
    final_price = original_price - discount_amount
    return final_price

# Test it
print(apply_discount(100, 20))  # Output: 80.0 (20% off)
print(apply_discount(50, 10))   # Output: 45.0 (10% off)
```

### Challenge: Function That Returns Multiple Values

Create a function that analyzes a list of numbers.

**Task**: Write a function named `analyze_numbers` that:
- Takes a list of numbers as a parameter
- Calculates the sum, average, and count
- Returns all three values

**Example Solution**:
```python
def analyze_numbers(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return total, average, count

# Test it
data = [10, 20, 30, 40]
total, avg, count = analyze_numbers(data)
print(f"Sum: {total}, Average: {avg}, Count: {count}")
# Output: Sum: 100, Average: 25.0, Count: 4
```

## Assessment

### Self-Check Questions

1. **What is a function and why are functions useful?**
   - A function is a reusable block of code that performs a task. Functions help you avoid repetition, organize code, and make programs more readable.

2. **How do you define a function in Python?**
   - Use the `def` keyword followed by the function name and parentheses: `def function_name(parameters):` then the function body.

3. **What's the difference between a parameter and an argument?**
   - A parameter is what you define in the function (e.g., `def add(a, b)`). An argument is the actual value you pass when calling the function (e.g., `add(3, 5)`).

4. **What does the `return` statement do?**
   - The `return` statement sends a value back from the function to the code that called it.

5. **Can a function have no parameters?**
   - Yes, you can write `def function_name():` with empty parentheses.

## Summary

Functions are essential for writing clean, organized code:

- **Define** functions with `def function_name():`
- **Use parameters** to pass data into functions
- **Use return statements** to send results back
- **Call functions** by name with arguments
- **Reuse code** by calling the same function multiple times

Functions help you break big problems into small, manageable pieces.

## Next Steps

- Write your own functions for daily tasks
- Experiment with functions that return different data types
- Explore built-in functions like `len()`, `sum()`, `max()`
- Look into variable scope (local vs global variables) in future lessons

---

*You're building great coding habits! Check out more lessons in the [Python Basics](index.md) section.*
