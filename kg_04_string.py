# Strings in python
X = "INDIA IS BEST"
Y = 'INDIA IS BEST' # can be defined using single or double quotes
print(X == Y) # they are functionaly equivalent

# we can wrap the double quote string in single quotes
print('Hi my name is "Vaibhav"')

# new line character using \n
hello = "Hello\nworld"
print(hello)

# slicing in python
HI = 'HELLO WORLD'
print(HI[9:11])

# length of a string
print(len(HI))

# using docstring for new line
Hi = """Hello
world"""
print(Hi)
print(hello == Hi)

# Strings are sequesnces of characters
s = 'Ariculate'
print(s[0])

# methods in string 
claim = 'Pluto is a planet!'
print (claim.upper()) # converts to upper case
print (claim.lower()) # converts to lower case
print (claim.title()) # converts to title case

print(claim.index('plan'))
print(claim.startswith('planet'))
print(claim.endswith('planet'))

words = claim.split() # splits the string into a list of words
print(words)

# spliting other than space
date = '17-04-2026'
day,month,year= date.split('-')

Join ='/'.join([year,month,day]) # join function in python
print(Join)

# concatination in python 
print(claim + ' In this solar syatem')
position = 9
print(claim + ' Which is on '+str(position)+'th position')