# Defining a Dictionary
numbers = {'one':1,'two':2,'three':3}
print(numbers['one'])
numbers['one']='pluto'
numbers['eleven']=11
print(numbers)

# deleting key and values from dictionary
numbers.pop('one','pluto')
numbers.popitem()
print(numbers)

# Python has dictionary comprehensions with a syntax similar to the list comprehensions
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
solar_system = {planet:planet[0] for planet in planets}
print(solar_system)

#The in operator tells us whether something is a key in the dictionary
print('Saturn' in solar_system)
print('Polar' in solar_system)

# .keys() & .values() function in python
print(solar_system.keys())
print(solar_system.values())

print(' '.join(sorted(solar_system.values())))


