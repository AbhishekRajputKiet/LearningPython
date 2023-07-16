# a=input("Enter a input: ")
# print(f"Table of {a} is  : ")
# try:
#     for i in range(1,11):
#         print(f"{int(a)} X {i} = {int(a*i)}")
# except:
#     print("Invalid input")
# print("it is execute when try statement is used in programe")


try:
    num = int(input("Enter a integer number :"))
    a=[6,3]
    print(a[num])
except ValueError:
    print("Number is not integer ")
except IndexError:
    print("Index error")


