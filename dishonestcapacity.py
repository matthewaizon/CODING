print('Enter TB or GB for the advertised unit:')
state = 0

# Calculate the amount that the advertised capacity lies:
while state == 0:
    unit = input('>').upper()
    if unit == 'TB':
        discrepancy = 1000000000000 / 1099511627776
        state = 1
    elif unit == 'GB':
        discrepancy = 1000000000 / 1073741824
        state = 1
    else:
        print('Unrecognized unit')
    

print('Enter the advertised capacity:')

advertised_capacity = input('>')
advertised_capacity = float(advertised_capacity)

# Calculate the real capacity, round it to the nearest hundredths,
# and convert it to a string so it can be concatenated:
real_capacity = str(round(advertised_capacity * discrepancy, 2))
print('The actual capacity is ' + real_capacity + ' ' + unit)