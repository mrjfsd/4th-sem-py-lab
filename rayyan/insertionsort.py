def insertionsort(arr):
  for i in range(1, len(arr)):
      j = i
      while arr[j-1]> arr[j] and j>0:
          arr[j-1], arr[j]= arr[j], arr[j-1]
          j-=1

arr=[]
n=int(input("Enter the no. of elements"))
for i in range(n):
    arr.append(int(input("Enter the elements")))
print("before sorting",arr)
insertionsort(arr)
print(arr)
