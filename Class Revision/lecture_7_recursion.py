def countdown(start):
    if start >= 0:
        print(start)
        countdown(start - 1)


number = int(input("Enter a number: "))
countdown(number)
