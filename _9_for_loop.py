# looping through string
print('looping through string')
for item in 'Hello' :
    print(item)

# looping through list
print('looping through list')
for item in [1,2,3,4,5]:
    print(item)


# looping using range
print('looping using range')
for item in range(2,5,2):  # (starting_position, limit, incrementer)
    print(item)



# practice
print('cart sum:')
prices = [20, 30, 40]
total = 0
for price in prices:
    total = total + price
print(total)
