try:

 num=int(input("enter number to check odd even"))
 if num%2==0:
    print(f"given number {num} is even number")
 else:
        print(f"given number {num} is odd number")
except:
    print("please write intiger number")


    #chatgpt method 
# Here are five different methods to check if a given number is odd or even in Python.

### Method 1: Using Modulus Operator

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

### Method 2: Using Bitwise AND Operator
num = int(input("Enter a number: "))
if num & 1 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")
# Explanation: In binary, even numbers have the least significant bit as `0`. The `& 1` operation checks if the least significant bit is `0` (even) or `1` (odd).

### Method 3: Using Division and Multiplication

num = int(input("Enter a number: "))
if (num // 2) * 2 == num:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

# Explanation: This method divides the number by 2, multiplies the quotient by 2, and checks if it equals the original number. If it does, the number is even; otherwise, it’s odd.

### Method 4: Using Ternary Operator (One-Line Solution)

num = int(input("Enter a number: "))
print(f"{num} is even." if num % 2 == 0 else f"{num} is odd.")

# Explanation: This is a concise way to check evenness or oddness using Python’s ternary (conditional) operator.

### Method 5: Using List Indexing

# ```python
num = int(input("Enter a number: "))
result = ["even", "odd"]
print(f"{num} is {result[num % 2]}.")
# ```

# Explanation: This method uses list indexing based on the remainder. If `num % 2` is `0`, it selects `"even"`; if `1`, it selects `"odd"`. 

# Each method will effectively determine whether the entered number is odd or even.