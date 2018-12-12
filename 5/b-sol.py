from helper import react_length
from sets import Set

with open('input') as f:
    str = f.readline().rstrip()

s = Set()
for char in str:
    s.add(char.lower())

shortest = len(str)
best = None

for char in s:
    l = react_length(str, char)
    if l < shortest:
        shortest = l
        best = char

print shortest
