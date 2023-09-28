# 4. Write a program to find the largest of three numbers.

print('Find out the largest number.')
first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
third_num = int(input('Enter third number: '))

# using max method
# largest_number = max(first_num, second_num, third_num)
# print('The largest number is: ', largest_number )

# using conditions

if first_num > second_num and first_num > third_num:
    print(f'The largest number is first number, which is :{first_num}')
elif second_num > first_num and second_num > third_num:
    print(f'The largest number is second number, which is :{second_num}')
else:
    print(f'The largest number is third number, which is :{third_num}')
