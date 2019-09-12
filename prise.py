def format_price(price):
    price = int(price)
    pr = f'Цена: {price} руб.'
    return pr


result = format_price(56.24)
print(result)
