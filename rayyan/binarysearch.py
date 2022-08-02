import matplotlib.pyplot as plt
import numpy as np
import time
start = time.time()
def binarysearch(arr, x, low, high):
    if high >= low:
        mid = low + (high - low) // 2
        if (arr[mid] == x):
            return mid
        elif (arr[mid] > x):
            return binarysearch(arr, x, low, mid - 1)
        else:
            return binarysearch(arr, x, mid + 1, high)
    else:
        return 1


arr = [3,4,5,6,7,8,9]
x = 4
res = binarysearch(arr,x,0,len(arr)-1)
if(res!= -1):
    print("element  found at index " +str(res))
else:
    print("element not found")
end = time.time()
print({end-start})
xpoints = np.arary([500,1000,1500,2000,2500,5000])
ypoints=np.array([0.00009,0.0010,0.0020,0.0030,0.0040,0.0050])
plt.plot(xpoints,ypoints)
plt.show()


