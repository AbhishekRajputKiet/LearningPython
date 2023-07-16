try:
    l=[2,3,5,7]
    i=int(input("Enter an number : "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always accepted")
    