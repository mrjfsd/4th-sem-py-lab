def selectionsort(a):
    n=len(a)
    for i in  range(n-2):
        min=i
        for j in range(i+1,n-1):
            if(a[j]<a[min]):
                temp=a[j]
                a[j]=a[min]
                a[min]=temp
arr=[]
n = int(input("Enter the range"))
for i in range(n):
    arr.append(int(input("enter the elements")))
print(arr)
print("before sorting",arr)
selectionsort(arr)
print("after sorting",arr)