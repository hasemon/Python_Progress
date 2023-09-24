# A shop has the four products ( pendrive, keyboard, mouse, and headphone).
# Take the prices of each product and print the total amount to pay.
# The shop offers 20% discount if total cost is more than 1000 tk.

pendrive_price = int(input('Enter pendrive price: '))
keyboard_price = int(input('Enter keyboard price: '))
mouse_price = int(input('Enter mouse price: '))
headphone_price = int(input('Enter headphone price: '))

total_price = pendrive_price + keyboard_price + mouse_price + headphone_price

print('Your total cost is: ', total_price, 'taka')

if total_price > 1000:
    discount_20_per = total_price * 20/100
    discounted_price = total_price - discount_20_per
    print('You got discount of: ', discount_20_per, 'taka')
    print('Your discounted price is: ', discounted_price, 'taka')
else:
    print('Please buy more than 1000 to get 20% discount.')