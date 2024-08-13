amount = int(input('enter you amount of bill : '))
if amount<=1000:
    discount = 10/100 * amount
elif amount>1000 and amount<=5000:
    discount = 10/100 * amount
elif amount>5000 and amount<=10000:
    discount = 10 / 100 * amount
else:
    discount = 10 / 100 * amount
payable_amount = amount-discount
print(f'discount: {discount}')
print(f'you need to pay: {payable_amount}')