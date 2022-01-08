# largest number in list
numList = [10,14,6,7,11,9]
big = 0
temp = 0
for item in numList:
    if item > temp:
        temp = item
print(temp)


# some useful list method
print('pop.........')
print(numList.pop()) # pop method retrive the last element of list, it also take index as parameter

print("sort..........")
numList.sort() # In order to sort the list
print(numList)

#print("clear ..............")
#numList.clear()
#print(numList)

print('index .....')
print(numList.index(10)) # getting index of any element that exit in the list

print('append ........')
numList.append(3) # add element to end of the list
print(numList)



# Nested list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0][1])