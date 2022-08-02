def linearsearch(arr,n,key):
    for i in range (n):
        if (arr[i] == key):
            return i
    return 0
arr = []
n = int(input("Enter the no of element"))
for i in range(n):
     arr.append(int(input("enter the elements")))
print("The array elements are: ",arr)
key = int(input("Enter the key element"))
res=linearsearch(arr,n,key)
if(res != 0):
    print("element not found")
else:
    print("element %d found at index %d" %(key,res))

