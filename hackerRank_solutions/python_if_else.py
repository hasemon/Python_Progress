# Given an integer, N , perform the following conditional actions:
# If N is odd, print "Weird"
# If N  is even and in the inclusive range of 2 to 5, print "Not Weird"
# If N is even and in the inclusive range of 6 to 20, print "Weird"
# If N is even and greater than 20, print "Not Weird"

n = int(input('Enter a number: '))

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0:
    if n in range(2, 5):
        print("Not Weird")
    elif n in range(6, 21):
        print("Weird")
    elif n > 20:
        print("Not Weird")

