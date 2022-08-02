def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
arr=[]
n= int(input("Enter the range of the list"))
for i in range(n):
    arr.append(int(input("Enter the elements")))
print("unsorted array",arr)
print("sorted array")
bubblesort(arr)
for i in range(len(arr)):
 print(arr[i],end=" ")