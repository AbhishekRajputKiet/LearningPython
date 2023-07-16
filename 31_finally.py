try:
    l=[2,3,5,7]
    i=int(input("Enter an number : "))
    print(l[i])
except:
    print("some error occured")
finally:
    print("I am always accepted") # it always execute if in side the function 
                                # function return at any conditon then finally function still executed
                                # but at that comdition print statement does not executed
                                # 
                                
