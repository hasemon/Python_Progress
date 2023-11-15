# Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village,
# and probably some good-looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!!
# german are coming!
# The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory,
# then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken...in this version you don't have to pay for stuff or add it up


# create stores
freelancers = {'name': 'freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100, 'grim reaper': 500,
               'minstrel': -15}
antiques = {'name': 'Antique Shop', 'french castle': 400, 'wooden grail': 3, 'scythe': 150, 'catapult': 75,
            'german joke': 5}
pet_shop = {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}

cart = {}
for shop in (freelancers, antiques, pet_shop):
    buy_item = input(f'Welcome to {shop["name"]}! what do you want to buy {shop}:').lower()
    cart.update({buy_item: shop.pop(buy_item)})
print(f'You Purchased {cart.keys()} Today it is all free. Have a nice day of mayhem!')
