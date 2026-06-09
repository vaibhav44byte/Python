import math
import math as mt
from math import * # import * makes all the module's variables directly accessible to you (without any dotted prefix).
print(math.pi)
print(math.log(32,2))
print(pi,log(32,2))

#Three tools for understanding strange objects
# 1: type() (what is this thing?)
print(type(math))
# 2: dir() (what can I do with this thing?)
print(dir(math))
# 3: help() (how do I use this thing?)
help(math.log)