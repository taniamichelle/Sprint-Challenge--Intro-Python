# The following list comprehension exercises will make use of the 
# defined Human class. 
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"<Human: {self.name}, {self.age}>"

humans = [
    Human("Alice", 29),
    Human("Bob", 32),
    Human("Charlie", 37),
    Human("Daphne", 30),
    Human("Eve", 26),
    Human("Frank", 18),
    Human("Glenn", 42),
    Human("Harrison", 12),
    Human("Igon", 41),
    Human("David", 31),
]
# print(humans)
h = Human("Joe", 49)
print('name of h', h.name)
print('age of h', h.age)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with 'D':
print("Starts with D: ")
a = [d.name for d in humans if d.name[0] == 'D']
# names = [n.name if n in humans if n.name.startswith('D')]
# print(names)
print(a)

# Write a list comprehension that creates a list of names of everyone
# whose name ends in "e".
print("Ends with e:")
b = [e.name for e in humans if e.name[-1] == 'e']
print(b)

# Write a list comprehension that creates a list of names of everyone
# whose name starts with any letter between 'C' and 'G' inclusive.
print("Starts between C and G, inclusive:")
c = [x.name for x in humans if x.name[0] == 'C' or x.name[0] =='D' or x.name[0] =='E' or x.name[0] =='F' or x.name[0] == 'G']
print(c)

# Write a list comprehension that creates a list of all the ages plus 10.
print("Ages plus 10:")
d = [a.age + 10 for a in humans]
print(d)

# Write a list comprehension that creates a list of strings which are the name
# joined to the age with a hyphen, for example "David-31", for all humans.
print("Name hyphen age:")
e = []
print(e)

# Write a list comprehension that creates a list of tuples containing name and
# age, for example ("David", 31), for everyone between the ages of 27 and 32,
# inclusive.
# res = list(map(eval, humans))
# print('humans tuple: ', res)
# print("Names and ages between 27 and 32:")
# f = [t for t in humans if 27 >= t.age >= 32]
# print(f)

# Write a list comprehension that creates a list of new Humans like the old
# list, except with all the names uppercase and the ages with 5 added to them.
# The "humans" list should be unmodified.
# print("All names uppercase:")
# g = humans.copy([u.name.upper() for u in humans + f.age + 5 for f in humans])
# print(g)

# Write a list comprehension that contains the square root of all the ages.
print("Square root of ages:")
import math
h = [r.sqrt]
print(h)
