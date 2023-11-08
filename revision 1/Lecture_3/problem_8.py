# 8. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# • Ask user for quantity. Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input("Enter quantity: "))
cost = int(input("Enter cost: "))

totalPrice = quantity * cost
discount = totalPrice * 10 / 100
priceWithDiscount = totalPrice - discount

if totalPrice > 1000:
    print("Price with 10% discount", priceWithDiscount)
else:
    print("Your cost is :", totalPrice)