menu = ['latte', 'chocolate chip muffin', 'pain au chocolat', 'tea']

stock = {
    'latte' : 1000,
    'chocolate chip muffin' : 600,
    'pain au chocolat': 800,
    'tea': 1000
}

price = {
    'latte' : 2.30,
    'chocolate chip muffin' : 3.00,
    'pain au chocolat' : 3.00,
    'tea' : 2.30
}

total_stock = 0

for x in menu:
    total_stock += stock[x] * price[x]

print(f"The total stock value is £{total_stock:.2f}")