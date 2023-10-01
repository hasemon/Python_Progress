quantity = int(input("Enter quantity: "))
cost = int(input("Enter cost: "))
discount = int(input("Enter discount percentage: "))

totalCost = (quantity * cost)
discountPercent = (totalCost * discount) / 100

priceWithDiscount = totalCost - discountPercent

if totalCost > 2000:
    print(f'Your Total Price with discount is : {priceWithDiscount}')
else:
    print(f'Your total price is : {totalCost}')



