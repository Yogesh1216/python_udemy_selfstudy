def sal(basic,allowance,deductions):
    print(f'basic : {basic}')
    print(f'allowance : {allowance}')
    print(f'deductions : {deductions}')
    total_sal = basic+allowance-deductions
    return total_sal

# we can pass random keyword arguments like this.
total = sal(allowance=6000,basic=8000,deductions=2000)
print(total)

