s1={2,4,7,9}
s2={3,5,8,2,4}

# print (s1.union(s2))
# s1.update(s2)
# print(s1)

# s1.intersection_update(s2)
# print(s1)

s1.symmetric_difference(s2)
print(s1.symmetric_difference(s2))
print(s1)

print(s1.isdisjoint(s2)) # No element is comoun
print(s1.issuperset(s2)) # element of s2 lies within the s1
print(s1.issubset(s2)) # each element of s1 lies within he s2

# s1.update(4)
# s1.add(2)
# s1.remove(9) # if 9 is not present then give errer
# s1.discard(9) # if 9 is not present then do not give errer
# s1.pop() #it remove last value randemly
# s1.clear() # its clear the sets