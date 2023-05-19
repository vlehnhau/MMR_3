import numpy as np
import Set as s



A = s.Set(["hund","katze","maus"])

# subset
print(A.subset(lambda x: len(x)==4))

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