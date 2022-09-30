def binarysearch(l,low,high,key):
    while low<=high:
        mid=(low+high)//2
        if l[mid]==key:
            return mid
        elif l[mid]>key:
            high=mid-1
        else:
            low=mid+1
    return -1
l=[]
low=0
n=len(l)-1
key=int(input("Enter element:"))
result=binarysearch(l,low,n,key)
if result==-1:
    print("Element not found")
else:
    print("Element found")
