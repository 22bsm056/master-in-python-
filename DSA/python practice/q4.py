#sum of given digit
num=int(input("enter digit to  see sum of his numbers:-"))
sum=0
n=str(num)
for i in n:
    dig=int(i)
    sum+=dig
print(sum)

#m2
num = int(input("Enter a number: "))

# Convert the number to a string, iterate over each digit, convert to int, and sum them
digit_sum = sum(int(digit) for digit in str(num))

print("Sum of digits:", digit_sum)


