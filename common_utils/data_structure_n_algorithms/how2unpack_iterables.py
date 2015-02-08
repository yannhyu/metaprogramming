#!/usr/bin/python -tt

stock_sold = [ 'IBM', 50, 92.4, (2012, 2, 14) ]
name, shares, price, (year, mon, _) = stock_sold

print('name:', name)
print('shares:', shares)
print('price:', price)
print('year:', year)
print('month:', mon)
