# 3. Write a program to read the age of a candidate and determine whether s/he is eligible for casting vote.

age = int(input("Enter age: "))

if age >= 18:
    print("You are a voter.")
else:
    print("You are not a voter.")