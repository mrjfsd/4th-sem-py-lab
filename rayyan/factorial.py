def factorial(n):
    if(n==1):
        return 1
    else:
        return (n*factorial(n-1))
n = int(input("Enter the factorial number"))
print("The factorial is ", n, ":",factorial(n))