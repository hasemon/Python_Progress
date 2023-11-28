
numberOfProduct = int(input("Enter the number of product you want: "))
productDict = {}

for i in range(numberOfProduct):
    buyPrice = int(input("Enter the buy price: "))
    profit = buyPrice * 0.2
    sellPrice = buyPrice + profit
    productDict.update({i + 1001: sellPrice})


print(productDict)

duplicateProductDict = productDict.copy()
print(duplicateProductDict)

newProducts = {2001: 'Suger', 2002: 'Salt', 2003: 'Rice'}
duplicateProductDict.update(newProducts)
print(duplicateProductDict)

newProducts.pop(2003)
print(newProducts.get(2002))
print(newProducts.keys())
print(newProducts.values())
print(newProducts.items())
newProducts.clear()