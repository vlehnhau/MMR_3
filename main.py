import numpy as np
import Set as s

# Aufgabe 3.1.1

A = s.Set(["hund", "katze", "maus"])

# subset
print(A.subset(lambda x: len(x) == 4))

# __iter__
for i in A:
    print(i)

# __contains__
if "hund" in A:
    print("wau")

# __len__
print(len(A))

# _getitem_
print(A[2])


# Aufgabe 3.1.2

def n_as_Set(n):
    if n == 0:
        return s.Set([])
    return n_as_Set(n - 1) | s.Set([n_as_Set(n - 1)])


print(n_as_Set(0))
print(n_as_Set(1))
print(n_as_Set(2))
print(n_as_Set(3))
print(n_as_Set(15))


print(str(s.Set([0]).power_set()))
my_set = s.Set([1, 2, 3])
print(my_set.power_set())