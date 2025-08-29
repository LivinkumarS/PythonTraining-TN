# a=[1,2,3,"Hi",True,False,3,4,5,6,7,8,9]
# a[3]="Hello"
# print(a[2:5])

# a.append(10)
# a.append(11)
# a.insert(4,0)
# a.pop()
# a.remove(3)
# a.remove(3)
# a.pop(6)

# b=[234,134,54,45,54,3,46,35,4,45,32]

# b.sort()
# b.reverse()

# print(b.index(33))

# lis1=[
#     1,
#     2,
#     3,
#     True,
#     False,
#     [
#         4,
#         5,
#         6,
#         [
#             "one","two","three"
#         ]
#     ]
# ]

# print(lis1[-1][-1][-1][1])


# tup1=(1,2,3,3,2,1)

# tup1[0]=-1

# print(tup1)

# set1={312,234,234,34,34,45}
# set2={32,34,56,99,234}

# print(set1.intersection(set2))
# print(set1.union(set2))

# dict1={
#     'name':"Vijay",
#     'age':54,
#     'isMarried':True
# }

# dict1['age']=55

# print(list(dict1.keys()))
# print(dict1.values())

lis1=[23,23,34,23,54,34,56,34,67,45,
      67,43,32,23,54,56,45,45,54,344]

print(list(set(lis1)))

for i in lis1:
    print(i-i)