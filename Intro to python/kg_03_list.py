planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
for planet in planets:

    print(planet , end=" ") #prints planets in same line with space in between

# loop for string
s = "steganograpHy is the practicE of conceaLing a file, message, image, or video within another fiLe, message, image, Or video."
msg = " "
for i in s:
    if i.isupper():
        print(i,end="")

# range function in python
for i in range (5): # for loop
    print("Hello World")

# while loop in python
i = 0
while i< 10:
    print(i, end=" ")
    i +=1
