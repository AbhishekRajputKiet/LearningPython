dic = {5 : "abhi" ,34 :"chirag", 23: "Akash",12:"Ritik",11:"Rajput"}
print(dic[5])
print(dic.get(9)) # this give output nune
# print(dic[9])       #this give errer
print(dic.keys())

for key in dic.keys():
    print(dic[key])
print(dic.items())
for key,val in dic.items():
    print(key,val)