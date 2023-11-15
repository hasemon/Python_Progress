# updating string
var1 = 'Hello World!'
print('updated string: ', var1[:6] + 'Python')

# capitalize: returns a copy of the string with only its first character capitalized.
str1 = "this is string example"
print('Capitalized its first character: ', str1.capitalize())

# find method: returns the index if found and -1 otherwise.
str2 = "this is string example"
str3 = "exam"
print(str2.find(str3))

# method - isalnum() : returns true if all characters in the string are alphanumeric and there is at least one
# character, false otherwise
str4 = "this2009"
print(str4.isalnum())
print(str2.isalnum())

# method - isalpha() : checks whether the string consists of alphabetic characters only.
str5 = "alphabetic characters only"
str6 = str5.replace(" ", "")  # Removes space from a string
print(str6.isalpha())
print(str5.isalpha())

# method - isdigit() : checks whether the string consists of digits only
strNum = "123456"
print(strNum.isdigit())

# method islower() checks whether all the case-based characters (letters) of the string are lowercase.
# method isupper() checks whether all the case-based characters (letters) of the string are uppercase.
str5l = str5.lower()
print(str5.islower())
print(str5l.isupper())
str5u = str5.upper()
print(str5u.islower())
print(str5u.isupper())
