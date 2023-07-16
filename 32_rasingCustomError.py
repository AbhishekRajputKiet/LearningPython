n=int(input("Enter a number between 5 to 9 : "))
if n<5 or n>9:
    raise ValueError("Value should be between 5 and 9")