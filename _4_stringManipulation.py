info = 'Learning python'
print(info[0]) # for accessing index value
print(info[0:3]) # left side of colon is starting position and right side of the color is how many char we take
print(info[0:]) # right side of colon value can be ommit, then it will print full string
print(info[:4]) # python interpreter will assign 0 if left side of color value is ommit,
newInfo = info[:] # it will assign full string to new variable
print(newInfo)
print(newInfo[0:-1])


# string formatting
firstName = 'abdul afe'
lastName = "Karim"
message = f'{firstName} [{lastName}] is a good boy'
print(message)


# string functions
print(len(firstName))  # to find length of string
print(firstName.upper())  # to hole string change as upper case
print(firstName.lower())  # to hole string change as upper case
print('bd' in firstName)  # to find anything in a string
print(firstName.title())  # first letter of every world will capital
print(firstName.capitalize())  # first letter of first word will capital
