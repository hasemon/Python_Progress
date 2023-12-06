# 7. Write two Python function as reverse() & palindromeCheck() to decide whether a passed number is a palindrome or not.


# reverse function

def reverseNum(number):
    newNumber = 0
    while number > 0:
        digit = number % 10
        newNumber = newNumber * 10 + digit
        number = number // 10
    return newNumber


def checkPalindrome(number):
    number1 = reverseNum(number)
    if number1 == number:
        Palindrome = True
    else:
        Palindrome = False
    return Palindrome


n = int(input("Enter a number to check for palindrome: "))
print(reverseNum(n))
output = checkPalindrome(n)
if output:
    print("The number is palindrome")
else:
    print('The number is not palindrome')
