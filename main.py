#doordash order calculator
import sys

orderlimit = 31
cartlimit = 26
minsub = 15
one = 1

sub = input('Subtotal: ')
if float(sub) < minsub:
    print('Subtotal too small. Add more items to cart.')   
    sub = input('Subtotal: ')
elif float(sub) > cartlimit:
    print('Cart Price Limit hit. Please be below $26!')
    sub = input('Subtotal: ')

fee = input('Fee: ')
if float(fee) < one:
    print('Please enter a fee!')
    sub = input('Fee: ')
    
if float(sub) + float(fee) > orderlimit:
    print('Subtotal + Fees too large. Please remove an item from your cart and retry.')
    sys.exit

if float(sub) + float(fee) < orderlimit:
    print('Cart validated. Calculating fees...')
    ordertotal = float(fee) + float(sub)
    discount = ordertotal * .60
    round(discount, 2)
    difference = ordertotal * .40
    round(difference, 2)
    print(f'Total price: {ordertotal}')
    print(f'Your payment owed is {round(discount, 2)}, and you saved {round(difference, 2)} on this order.')