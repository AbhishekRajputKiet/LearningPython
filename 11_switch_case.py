x=int(input("Enter a number : "))

match x :
    case 0:
        print("x is zero.")
    case 1:
        print("x is one.")
    case 2:
        print("X is two.")
    case _ if x!=50:
        print(x," is not 50")
    case _ if x==50:
        print(x," is 50")
    case _:
        print("x is defoult.")