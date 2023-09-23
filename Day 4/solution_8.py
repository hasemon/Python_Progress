# 8. A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
# • Ask user for quantity. Suppose, one unit will cost 100. Judge and print total cost for user.

quantity = int(input('Product Quantity: '))
cost = int(input('Product Price: '))

total_cost = quantity * cost

print('Your total cost is: ', total_cost, '$')
if total_cost >= 1000:
    print('You are getting 10% discount.')
    discount = total_cost * 10 / 100
    price_with_discount = total_cost - discount
    print('Your discounted price is: ', price_with_discount, '$')
else:
    print('Buy more than 1000$ to get 10% discount.')

print('Thanks for shopping with us.')
