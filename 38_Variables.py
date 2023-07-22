x=4
print(x)
def value():
    x=6
    
    print(f"local variable is {x}")
print(f"Global variable is {x}")
value()
print(f"Global variable is {x}")

# local variable can not access outside the function 
# global variable can not be change inside the function 

