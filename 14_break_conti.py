n=int(input("Enter a number : "))

print("by continue statemnt")
for i in range (1,n+1):
    if i==5 :
        continue
    print(i)

print("by break statemnt")
for j in range (1,n+1):
    if j==5:
        break
    print(j)
