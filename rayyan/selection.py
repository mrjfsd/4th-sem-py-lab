def selectionsort(a):
    n=len(a)
    for i in  range(n-2):
        min=i
        for j in range(i+1,n-1):
            if(a[j]<a[min]):
                temp=a[j]
                a[j]=a[min]
                a[min]=temp
arr=[34,46,70,43,27,41,43]
print("before sorting",arr)
selectionsort(arr)
print("after sorting",arr)
