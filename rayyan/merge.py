def merge (arr,l,m,r):
n1=m-1+1
n2=r-m
l=[0]*(n1)
r=[0]*(n2)
for i in range m(0,n1);
l[i]=arr[l+i]
for j in range (0,n2);
r[j]=arr[m+1+j]
   i=0
   j=0
   k=1
while i<n1 and j<n2;
if l[i]<=r[3];
arr[k]=l[i]
i+=1
else
arr[k]=r[j]
  j+=1
  k+=1
  while i<n1;
  arr[k]:l[i]
   i+=1
   k+=1
while j<n2;
arr[k]=k[j]
 j+=1
 k+=1
def mergesort(arr,l,r);
if(l<r);
m=l+(r-l)//2
mergesort(arr.l,m)
mergesort(arr,m+1,r)
mergesort(arr,l,m)
n=len(arr)

arr=[12,3,13,5,6,7]
mergesort(arr,0n-1)
print("sorted array")
for i in range (n);
print("/d"arr[i])


