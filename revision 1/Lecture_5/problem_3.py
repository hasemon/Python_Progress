# 3. Create a list of marks of ten students.
# • Find the largest and smallest mark in the list.
# • Find the average mark of the students.
# • Sort the marks in ascending order.
# • Sort the marks in descending order.
# • Remove the smallest mark from the list.
# • Insert the average mark at the mid-position of the list.
# • Create another list of five students’ mark and merge the two lists.

marks = [2, 5, 3, 2, 1, 6, 7, 7, 8, 10]
smallestMarks = min(marks)
print('Smallest mark is :', smallestMarks)
largestMarks = max(marks)
print('Largest mark is :', largestMarks)
marks.sort()
print('Sorted marks :', marks)
marks.sort(reverse=True)
print('Sorted is descending order: ', marks)

marks.remove(smallestMarks)
print('Without smallest mark: ', marks)

average = sum(marks) // len(marks)
middleIndex = len(marks) // 2
marks.insert(middleIndex, average)
print('Marks in the middle of a list: ', marks)

marks2 = [3, 5, 6, 7, 8]

marks.extend(marks2)
print(marks)
