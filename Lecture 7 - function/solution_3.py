# 3. Write a Python function to sum all the numbers in a list.

small_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
big_list = [100, 200, 300, 400]
ultra_big_list = [100000, 2005900, 3000980843, 40078394]


def sum_of_list(given_list):
    return sum(given_list)


# alternate way
def sum_list(l_list):
    sumOfList = 0
    for i in l_list:
        sumOfList += i
    return sumOfList


print('Sum of small list: ', sum_list(small_list))
print('Sum of big list: ', sum_of_list(big_list))
print('Sum of ultra big list: ', sum_of_list(ultra_big_list))
