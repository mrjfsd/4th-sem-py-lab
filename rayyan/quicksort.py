def partion(a,l,r):
    pivot,ptr=a[r],l
    for i in range(l,r):
        if a[i]<=pivot:
            a[i],a[ptr]=a[ptr],a[i]
            ptr+=1
    a[ptr],a[r]=a[r],a[ptr]
    return ptr
def qs(l,r,a):
    if (len(a)==1):
      return a
    if (l<r):
      pi=partion(a,l,r)
      qs(l,pi-1,a)
      qs(pi+1,r,a)
      return a
a=[3,0,2,9,8,7,5]
print("Before sorting",a)
size= len(a)
print("after sorting",qs(0,size-1,a))


