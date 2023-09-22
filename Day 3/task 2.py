price = int(input('Enter Price: '))
discount_per = int(input('Discount Percent: '))

discount = price * discount_per / 100
price_with_discount = price - discount

print('Price with Discount: ', price_with_discount)
