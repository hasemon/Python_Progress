emSalaries = [1000, 200, 300, 400, 500, 600, 700, 800, 500, 300]

highestSalary = max(emSalaries)
lowestSalary = min(emSalaries)
print('#1')
print("The highest salary:", highestSalary, 'and the lowest salary:', lowestSalary)

totalSalaries = 0
for salary in emSalaries:
    totalSalaries += salary

averageSalary = totalSalaries // len(emSalaries)
print('#2')
print('The average salary of employees is:', averageSalary)

emSalaries.sort(reverse=True)
print('#3')
print('Descending order of salaries is:', emSalaries)

midPos = len(emSalaries) // 2
emSalaries.insert(midPos, averageSalary)
print('#4')
print('Average salary in the mid position: ', emSalaries)

emSalaries2 = [300, 100, 200, 400, 550]

emSalaries.extend(emSalaries2)
print('#5')
print('Merged two salary list :', emSalaries)


