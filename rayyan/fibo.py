def fib(a1):
    if a1<=1:
        return a1
    else:
        return (fib(a1-1)+fib(a1-2))
a = (int(input("Enter the number : ")))
if a<=1:
     print("Please enter a positive value")
else:
    print("fib series : ")
for i in range(a):
    print(fib(i))