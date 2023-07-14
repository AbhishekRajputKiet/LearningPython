
# default argument 
def average(a=9 , b=1):
    print ("Averager of a or b is : ",(a+b)/2)

average(1,4) # ans is 2.5
average(a=3) 
average(b=3) # ave=(9+3)/2
average(5)  #  ave=(5+1)/2

# keyword argument :- order does not natter

def name (fname,mname="Jhon",lname="Whatson"):
    print("Hello, ",fname,mname,lname)
name(lname="Raj",fname="abhi") # ans is : abhi jhon Raj

# required argument : give complete value to function

# variable length argument 
# it take value as tuple
def average(*number):
    sum=0
    for i in number:
        sum=sum+i
    print("Average of two number : ",sum/len(number))
average(3,4,6,7,8)

#for dictionary
def name(**name):
    print("Hello",name["fname"],name["lname"],name["mname"])
name(mname="abhi",fname="kumar",lname="raj")