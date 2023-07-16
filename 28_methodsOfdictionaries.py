ep1= {32:4 , 24:6,39:9,38:1}
ep2 ={89:2,78:7,54:5}
# ep1.update(ep2)
# print(ep1)

ep1.pop(38)
print(ep1)
del ep2[54]
print(ep2)

ep1.clear()
print(ep1)
