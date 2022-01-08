is_hot = False
is_cold = True

if is_hot:
    print("It's hot day")
elif is_cold:
    print("It's cold day")
else:
    print("something went wrong")


housePrice = 10000000
goodPrice = False
if goodPrice:
    downPrint = (housePrice/100) * 10
else:
    downPrint = (housePrice/100) * 20


print(f'Down Payment:{downPrint}')