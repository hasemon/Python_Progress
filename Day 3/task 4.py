# A shop has the four products (pendrive, keyboard, mouse, and headphone).
# Take the prices and number of units for each product.
# Print the total amount to pay.
# The shop offers 25% discount if total cost is more than 2000 tk.


total_pendrive_price = 0
total_keyboard_price = 0
total_mouse_price = 0
total_headphone_price = 0

pendrive_unit = int(input('Pendrive units: '))
if pendrive_unit > 0:
    pendrive_price = int(input('Pendrive price: '))
    total_pendrive_price = pendrive_unit * pendrive_price

keyboard_unit = int(input('Keyboard units: '))
if keyboard_unit > 0:
    keyboard_price = int(input('Keyboard price: '))
    total_keyboard_price = keyboard_unit * keyboard_price

mouse_unit = int(input('Mouse units: '))
if mouse_unit > 0:
    mouse_price = int(input('Mouse price: '))
    total_mouse_price = mouse_unit * mouse_price

headphone_unit = int(input('Headphone units: '))
if headphone_unit > 0:
    headphone_price = int(input('Headphone price: '))
    total_headphone_price = headphone_unit * headphone_price

total_price = total_pendrive_price + total_keyboard_price + total_mouse_price + total_headphone_price

print('Total cost is: ', total_price, 'taka')

if total_price >= 2000:
    discount = total_price * 25 / 100
    print('You got discount of: ', discount, 'taka')
    print('Your discounted price is: ', total_price - discount, 'taka')
else:
    print('Please buy more than 2000 to get 25% discount.')
