a=[]
n=int(input("Enter the size of list:"))
for i in range(n):
    ele=int(input("Enter element:"))
    a.append(ele)
    for i in range(1,len(a)):
        j=i-1
        next_element=a[i]
        while(a[j]>next_element) and (j>=0):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=next_element
print(a)