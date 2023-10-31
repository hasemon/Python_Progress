# 4. Write a Python program to print the even numbers from a given list.
a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_list = [100, 144, 155, 135, 300, 450]


def even_numbers(n):
    even_numbers_list = []
    for num in n:
        if num % 2 == 0:
            even_numbers_list.append(num)
    return even_numbers_list


small_list_result = even_numbers(a_list)
big_list_result = even_numbers(b_list)

print('Even numbers:', small_list_result)
print('Even numbers:', big_list_result)
