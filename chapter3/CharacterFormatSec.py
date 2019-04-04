width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'

print('='*(int(width)))
print(header_format % (item_width, 'Item', price_width, 'Price'))
print('-'*(int(width)))

print(format % (int(item_width), 'Apples', int(price_width), 0.4))
print(format % (int(item_width), 'Pears', int(price_width), 0.5))
print(format % (int(item_width), 'Cantaloupes', int(price_width), 1.92))
print(format % (int(item_width), 'Dried Apricots (16 oz.)', int(price_width), 8))
print(format % (int(item_width), 'Prunes (4 lbs.)', int(price_width), 12))

print('='*(int(width)))


