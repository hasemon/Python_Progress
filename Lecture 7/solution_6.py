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
output = checkPalindrome(n)
if output:
    print("The number is palindrome")
else:
    print('The number is not palindrome')

