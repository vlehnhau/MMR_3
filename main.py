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


def binomialCoefficients(num):
    power = s.Set(list(range(num))).power_set()
    return_val = []

    if num == 0:
        return [1]

    return_val.append(1)

    for k in range(1, num + 1):
        counter = 0
        for element in power:
            if len(element) == k:
                counter += 1
        return_val.append(counter)

    return return_val

print(s.Set(list(range(3))).power_set())
print(binomialCoefficients(3))

# Aufgabe 3.1.3

a = s.Set([1,2,3])
b = s.Set([4,5,6])

print(a*b)

#Aufgabe 3.1.5

# persons = s.Set(["Alice", "Bob", "Charles", "Denise", "Eric"])
# likes = s.Relation([("Alice", "Bob"), ("Alice", "Denise"), ("Bob", "Alice"), ("Denise", "Charles"), ("Eric", "Eric")])
# testLikes = s.XmagY(persons, likes)
# testLikes.addLike("Denise", "Eric")
#
# print(testLikes.pLikes("Alice"))
# print(testLikes.pIsLikedBy("Alice"))
# print(testLikes.checkEquivalenceRelation(persons))
#
# persons2 = s.Set(["A", "B"])
# likes2 = s.Relation([("A", "A"), ("A", "B"), ("B", "A"), ("B", "B")])
# testLikes2 = s.XmagY(persons2, likes2)
# print(testLikes2.checkEquivalenceRelation(persons2))
#
#
# n = s.smallerEqual()
# print(str(n))

print("Beziehungen")
relationship = s.Relationships()
print(relationship)
# print(type(relationship))
print(relationship.checkEquivalenceRelation(s.Set(["Alice", "Bob", "Charles", "Denise", "Eric"])))

print("Ordnungen. SmallerEqual")
ordersSmallerEqual = s.Orders("smallerEqual")
print(ordersSmallerEqual)
print(ordersSmallerEqual.checkEquivalenceRelation(s.Set(list(range(0,101)))))

print("Ordnungen. Smaller")
ordersSmaller = s.Orders("smaller")
print(ordersSmaller)
print(ordersSmaller.checkEquivalenceRelation(s.Set(list(range(0,101)))))

print("Ordnungen. Equal")
ordersEqual = s.Orders("equal")
print(ordersEqual)
print(ordersEqual.checkEquivalenceRelation(s.Set(list(range(0,101)))))

print("Restklassenring")
rest5 = s.Remainder(5)
print(rest5)
print(rest5.checkEquivalenceRelation(s.Set(list(range(0,101)))))



print(s.equivalenceClasses(s.Relation([(1,1),(1,2),(2,2),(2,1),(3,3),(3,4),(4,4),(4,3)]), s.Set([1,2,3,4])))