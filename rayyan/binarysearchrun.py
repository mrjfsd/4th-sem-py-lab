import time
start = time.time()
def binarysearch(arr, n, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if (arr[mid] == n):
            return mid
        elif (arr[mid] > n):
            return binarysearch(arr, n, low, mid - 1)
        else:
            return binarysearch(arr, n, mid + 1, high)
    else:
        return 1


arr = []
n = (int(input("enter the key element")))
x = int(input("enter the range for the elements  :"))
for i in range(x):
  arr.append(int(input("store the element")))
n = (int(input("Search the key element")))
arr = binarysearch(arr,n,0,len(arr)-1)
if(arr!= -1):
    print("element  found at index  " +str(arr))
else:
    print("element not found")
end = time.time()
print({end-start})


