def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)
print(factorial(4))



def fibo(num):
    if num==0 :
        return 0
    elif num==1 or num==2:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)
num=10
print(fibo(num))
    

def Fibonacci(n):

	if n == 0:
		return 0

	elif n == 1 or n == 2:
		return 1

	else:
		return Fibonacci(n-1) + Fibonacci(n-2)

print(Fibonacci(9))

    