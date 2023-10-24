# Example #1: Simple function to say Hello to a given name ###
def greetings(name):
  # Code to execute
  print("Hello {}".format(name))
  # The above is how we format strings using str.format() function 
  # There are other ways to format strings such as the following:
  # print(f"Hello {name}")
  # Read more about string formatting in the following link
  # https://realpython.com/python-string-formatting/#3-string-interpolation-f-strings-python-36

# We need to call the greetings function and provide an input 
greetings("Tom")
greetings("Jane")

# Example #2: Function to ask user for two numbers
#             and print the sum of the two numbers
def sum_two_numbers():
  # These two variables are defined inside the scope of the function
  print("Summing two numbers")
  number1 = int(input("Please input the first number: "))
  number2 = int(input("Please input the second number: "))
  sum = number1 + number2
  print(f"Sum of two numbers is {sum}" )

sum_two_numbers()

# We cannot call number1 or number2 outside of the function
# Comment the line below to remove num3
print(number1)

### A function that substracts num1 by num2
def subtract(num1, num2):
  return num1 - num2

# These two variables are defined outside the scope of the function 
print("Substrating two numbers")
number3 = int(input("Please input the first number: "))
number4 = int(input("Please input the second number: "))

# We can call the function and set the result returned into a variable
result = subtract(number2, number3)
print("The result is {}".format(result))
