
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales_w2.append(int(input('Input last day sales: ')))

sales = sales_w1 + sales_w2


worst_day = min(sales) * 1.5
best_day = max(sales) * 1.5

print(f'Worst day sales $ {worst_day}')
print(f'Best day sales $ {best_day}')
print(f'Total sales ${worst_day + best_day}')

