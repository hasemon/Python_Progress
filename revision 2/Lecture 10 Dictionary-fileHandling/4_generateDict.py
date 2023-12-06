# 4. Write a Python script to generate and print a dictionary that contains a number (between 1 and n)
# in the form (x, x*x).


numDict = {}
number = int(input('Enter a number: '))

for num in range(1, number + 1):
    numDict.update({num: num ** 2})

print(numDict)
