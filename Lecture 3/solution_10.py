# 10. Write a program to read 10 numbers from the keyboard and find their sum and average.

print('Enter your favourite 10 numbers...')
sumOfNumbers = 0
i = 1
while i <= 10:
    numbers = int(input(f'Enter {i}th number: '))
    sumOfNumbers += numbers
    i += 1

average = sumOfNumbers // 10
print('Sum of these ten numbers is: ', sumOfNumbers)
print('Average of this ten numbers is: ', average)

