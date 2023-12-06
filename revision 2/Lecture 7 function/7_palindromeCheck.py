# 7. Write two Python function as reverse() & palindromeCheck() to decide whether a passed number is a palindrome or not.

def reverseNum(num):
    reversedNum = 0
    while num > 0:
        digit = num % 10
        reversedNum = reversedNum * 10 + digit
        num = num // 10
    return reversedNum


originalNumber = int(input('Enter a number to check palindrome: '))
reverseNumber = reverseNum(originalNumber)
if reverseNumber == originalNumber:
    print('This is palindrome.')
else:
    print('This is not a palindrome.')
