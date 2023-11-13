# 10. Write a program to read 10 numbers from the keyboard and find their sum and average.

sumOfNumbers = 0
i = 1
while i <= 10:
    number = int(input(f'Enter {i}th number: '))
    sumOfNumbers += number
    i += 1

averageNumber = sumOfNumbers // 10


print('The sum of ten numbers: ', sumOfNumbers)
print('The average number ', averageNumber)