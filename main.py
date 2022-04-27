#doordash order calculator
import csv
import sys
import pyperclip as pc

from soupsieve import select

orderlimit = 31
cartlimit = 26
minsub = 15
one = 1
handles = open('payments.csv')

while True:
    print('Welcome to evans DD calc.')
    selection = int(input(''' 
1. Calculate Fees
2. Payment Info
3. Quit App
    '''))

    if int(selection) == 1:
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
            pc.copy(round(ordertotal, 2))

    elif int(selection) == 2:
        handles = open('payments.csv')
        read_data = csv.reader(handles) #string asks if "read_data" can read "handles" in comma separated values
        data = list(read_data) # all data is in csv
        cashapp = data[0]
        venmo = data[1]
        zelle = data[2]

        print(f'''
Cashapp: {cashapp[1]}
Venmo: {venmo[1]}
Zelle: {zelle[1]}

        ''')


    elif int(selection) == 3:
        print(f'Quitting app.')
        break


    else:
        print('Number selection not recognized. Try again.')

