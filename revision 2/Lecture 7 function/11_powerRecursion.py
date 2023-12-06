# 11. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.

# Define a function named 'power' that takes two parameters: 'base' and 'nPower'.
def power(base, nPower):
    # Check if the power is 0. If so, return 1 (base case).
    if nPower == 0:
        return 1
    # If the power is not 0, calculate the result using recursion.
    else:
        # Return the product of 'base' and the result of the function called with reduced power.
        return base * power(base, nPower - 1)


# Call the 'power' function with base=2 and nPower=4 and print the result.
a = int(input('Enter base number: '))
b = int(input('Enter power number: '))
print(power(a, b))

# explanation
# power(2, 4) = 2 * power(2, 3)
#             = 2 * (2 * power(2, 2))
#             = 2 * (2 * (2 * power(2, 1)))
#             = 2 * (2 * (2 * (2 * power(2, 0))))
#             = 2 * (2 * (2 * (2 * 1)))  # Base case is reached, and the recursion starts to resolve backward.
#             = 16
