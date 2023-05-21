import math


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

