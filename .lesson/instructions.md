## **Python Programming Concepts**

### **1. Functions:**
```python
def greetings(name):
    print("Hello {}".format(name))

greetings("Tom")
greetings("Jane")
```

- **Scope:** Variables inside a function are in local scope, those outside are in global scope.
- **Returning Values:** Using the `return` keyword to send back results.
  
### **2. Loops and Iteration:**
```python
fruits = ['Apple', 'Orange', 'Banana']
for fruit in fruits:
    print(fruit)

for number in range(5, 21, 2):
    print(number)
```

- **Control Statements:** `break` to exit, `continue` to skip iterations in a loop.

### **3. Lists:**
```python
class_names = ["Thomas", "Henderson", "Stephanie", "Tim"]
class_names.append("John")
class_names.insert(0, "Angela")
class_names.sort()
class_names.reverse()
```

- **Accessing Items:** Using indices.
- **List Methods:** `append()`, `insert()`, `sort()`, `reverse()`, `extend()`.

### **4. Boolean Operators:**
```python
if (age < 12 or age >= 65):
    print("You can enter for free")
elif (age <= 12 and age <= 18):
    print("You need to pay $8")
else:
    print("You need to pay $16")
```

- **Conditional Statements:** `if`, `elif`, and `else`.
- **Nested Conditionals and Multiple Ifs.**

### **Note:**
- Variables have scope, defining the region where they can be accessed or modified.
- Correct usage of conditional operators is crucial for implementing logic.
- Each element in a list can be accessed using its index, starting from 0.
- Functions can be used to encapsulate and reuse code, and they can return values using the `return` keyword.
