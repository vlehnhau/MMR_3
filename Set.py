import math

import Set


class Set:
    data: list

    def __init__(self, elements: list):
        self.data = elements

    def __str__(self):
        if not self.data:
            return "∅"
        return_val = "{"
        for i in range(len(self.data) - 1):
            return_val = return_val + str(self.data[i]) + ", "
        return_val = return_val + str(self.data[len(self.data) - 1]) + "}"
        return return_val

    def __repr__(self):
        return str(self)

    def __add__(self, other):
        return_val = self.data
        for i in other:
            if i not in return_val:
                return_val.append(i)
        return Set(return_val)

    def __or__(self, other):
        return_val = self.data.copy()
        for element in other:
            if element not in return_val:
                return_val.append(element)
        return Set(return_val)

    def __and__(self, other):
        return_val = []
        for i in self.data:
            if i in other:
                return_val.append(i)
        return Set(return_val)

    def __sub__(self, other):
        return_val = []
        for i in self.data:
            if i not in other:
                return_val.append(i)
        return Set(return_val)

    def subset(self, f: callable):
        return_val = []
        for i in self.data:
            if f(i):
                return_val.append(i)
        return Set(return_val)

    def __iter__(self):
        return iter(self.data)

    def __contains__(self, item):
        return self.data.__contains__(item)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data.__getitem__(item)

    def power_set(self):
        if not self.data:
            return Set([Set([])])
        element = self.data.pop()
        prev_power_set = Set(self.data).power_set()
        return prev_power_set | Set([subset | Set([element]) for subset in prev_power_set])

    def __mul__(self, other):
        return_val = []
        set_a = self.data
        set_b = other.data
        for a in set_a:
            for b in set_b:
                return_val.append((a, b))
        return xSet(return_val)


class xSet(Set):
    pass

class Relation(xSet):
    def checkReflexivity(self, set: Set):
        for s in set:
            if not ((s,s) in self):
                return False
        return True

    def checkSymmetry(self):
        for t in self:
            if not ((t[1], t[0]) in self):
                return False
        return True

    def checkTransitivity(self):
        for t1 in self:
            for t2 in self:
                if ((t1[0] == t2[1])) and not ((t1[1],t2[0]) in self):
                    return False
            return True

    def checkEquivalenceRelation(self, set: Set):
        if self.checkTransitivity() and self.checkSymmetry() and self.checkReflexivity(set):
            return True
        else:
            return False



# class XmagY(Relation):
#     def __init__(self, people: list, likes: Relation):
#         super().__init__(people)
#         self.likes = likes
#
#     def addLike(self,p1,p2):
#         if p1 and p2 in self:
#             if not (p1,p2) in self.likes:
#                 self.likes.__add__((p1,p2))
#         else:
#             print("Person nicht in Menge")
#
#     def pLikes(self,p):
#         self.pLikes = Set([])
#         for l in self.likes:
#             if (p == l[0]):
#                 self.pLikes = self.pLikes | Set([l[1]])
#         return self.pLikes
#
#     def pIsLikedBy(self,p):
#         self.pLikes = Set([])
#         for l in self.likes:
#             if (p == l[1]):
#                 self.pLikes = self.pLikes | Set([l[0]])
#         return self.pLikes
#
#     def checkEquivalenceRelation(self, set: Set):
#         return self.likes.checkEquivalenceRelation(set)
#
#
# class smallerEqual(Relation):
#     def __init__(self):
#         relation = Set([])
#         for a in self:
#             for b in self:
#                 if a <= b:
#                     relation = relation | Set([a,b])
#         super().__init__(relation)



def Relationships():
    #Sehr unsicher wie genau das umgesetzte werden soll
    persons = Set(["Alice", "Bob", "Charles", "Denise", "Eric"])
    # likes = Set([Set("Bob", "Charles", "Denise"), ("Eric", "Charles"), (), ("Charles", "Bob"), Set(["Eric"])])                             #Likes[0]: Perosnen die "Alice" mag
    likes = Set([Set(["Bob", "Charles", "Denise"]), Set(["Eric", "Charles", "Alice"]), Set([]), Set(["Charles", "Bob"]), Set(["Eric"])])
    result = Relation([])
    for l in range(0, len(persons)):
        for p in likes[l]:
            # print(type(result))
            # result = result | Relation([(persons[l], p)])
            result.__add__(Relation([(persons[l], p)]))
            # print(type(result))
    return result


def Orders(type: str):
    numbers = list(range(0,101))
    numbersSet = Set(numbers)
    result = Relation([])
    if type == "smallerEqual":
        for ni1 in numbers:
            for ni2 in numbers:
                # print("test")
                if  numbersSet[ni1] <= numbersSet[ni2]:
                    result.__add__(Relation([(numbersSet[ni1], numbersSet[ni2])]))
                    # print("test2")
        return result

    elif type == "smaller":
        for ni1 in numbers:
            for ni2 in numbers:
                if numbersSet[ni1] < numbersSet[ni2]:
                    result.__add__(Relation([(numbersSet[ni1], numbersSet[ni2])]))
        return result

    elif type == "equal":
        for ni1 in numbers:
            for ni2 in numbers:
                if numbersSet[ni1] == numbersSet[ni2]:
                    result.__add__(Relation([(numbersSet[ni1], numbersSet[ni2])]))
        return result

    else:
        print("type must be: smallerEqual, smaller or equal")

def Remainder(m: int):
    numbers = list(range(0,101))
    numbersSet = Set(numbers)
    result = Relation([])
    for ni1 in numbers:
        for ni2 in numbers:
            if (numbersSet[ni1] - numbersSet[ni2]) % m == 0:
                result.__add__(Relation([(numbersSet[ni1], numbersSet[ni2])]))
    return result



#Verstehe nicht warum das nicht funktioniert
def equivalenceClasses(relation: Relation, set: Set):
    if relation.checkEquivalenceRelation(set):
        classes = Set([])
        for element in relation:
            found = False
            a = element[0]
            b = element[1]
            for i in range(len(classes)):
                if a in classes[i] or b in classes[i]:
                        classes[i].__add__(element)
                        found = True
                        break
            if not found:
                classes.__add__(Set([(element)]))
        return classes
    else:
        print("Relation ist keine Äquivalenzrelation")
