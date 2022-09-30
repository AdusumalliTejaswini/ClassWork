def binarysearch(l,min,max,key):
    if min<=max:
        mid=(min+max)//2
        if l[mid]==key:
            return mid
        elif l[mid]<key:
            return binarysearch(l,mid+1,max,key)
        else:
            return binarysearch(l,min,mid-1,key)
    return -1
l=[]
n=int(input("enter the size:"))
for i in range(n):
     e=int(input("enter element:"))
     l.append(e)
     l=sorted(l)
print(l)
min=0
max=len(l)-1
key=int(input("Enter element:"))
res=binarysearch(l,min,n,key)
if res==-1:
    print("Element not found")
else:
    print("Element found at:",res+1)