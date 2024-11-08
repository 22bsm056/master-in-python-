#Certainly! Here are five different methods to reverse a 4-digit number in Python.

### Method 1: String Slicing

num = int(input("Enter a 4-digit number: "))
if 1000 <= num <= 9999:
    reversed_num = int(str(num)[::-1])
    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid 4-digit number.")
### Method 2: Mathematical Approach (Using Modulus and Division)

num = int(input("Enter a 4-digit number: "))
if 1000 <= num <= 9999:
    digit1 = num % 10
    digit2 = (num // 10) % 10
    digit3 = (num // 100) % 10
    digit4 = num // 1000
    reversed_num = digit1 * 1000 + digit2 * 100 + digit3 * 10 + digit4
    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid 4-digit number.")

### Method 3: Using a Loop (While Loop)

num = int(input("Enter a 4-digit number: "))
if 1000 <= num <= 9999:
    reversed_num = 0
    while num > 0:
        last_digit = num % 10
        reversed_num = reversed_num * 10 + last_digit
        num = num // 10
    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid 4-digit number.")

### Method 4: Using List Reversal

num = int(input("Enter a 4-digit number: "))
if 1000 <= num <= 9999:
    num_list = list(str(num))      # Convert number to list of digits
    num_list.reverse()              # Reverse the list
    reversed_num = int("".join(num_list))  # Join list back to string and convert to int
    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid 4-digit number.")

### Method 5: Using Recursion

def reverse_number(num, rev=0):
    if num == 0:
        return rev
    else:
        rev = (rev * 10) + (num % 10)
        return reverse_number(num // 10, rev)

num = int(input("Enter a 4-digit number: "))
if 1000 <= num <= 9999:
    reversed_num = reverse_number(num)
    print("Reversed number:", reversed_num)
else:
    print("Please enter a valid 4-digit number.")
#Each of these methods will reverse a 4-digit number entered by the user, showcasing different approaches to achieve the same result.