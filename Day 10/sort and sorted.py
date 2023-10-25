my_list = [1, 5, 3, 7, 2]
my_dict = {'car': 4, 'dog': 2, 'add': 3, 'bee': 1}
my_tuple = ('d', 'c', 'e', 'a', 'b')
my_string = 'python'

my_list.sort()
print(my_list, 'sort original list in ascending order, not returns any')

sorted_list = sorted(my_list)
print(sorted_list, 'returns new list after sorting in ascending order')
sorted_list_descending = sorted(my_list, reverse=True)
print(sorted_list_descending, 'returns new list after sorting in descending order')

sorted_dict = sorted(my_dict)
sorted_dict_items = sorted(my_dict.items())

print(sorted_dict_items, 'sorted dictionary alphabetically and change type to tuple')
print(sorted_dict, 'sorted dictionary alphabetically and change the type to list')

sorted_tuple = sorted(my_tuple)
print(sorted_tuple, 'sorted tuple alphabetically and change the type to list')

sorted_string = sorted(my_string)
print(sorted_string, 'sorted string by ANSI code and change the type to list')

