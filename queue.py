import sys
from array import *
queue=array('i',[])
def enqueue():
    element=int(input("enter the element:"))
    queue.append(element)
    print("Element is added to queue")
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e=queue.pop(0)
        print("Removed element is",e)
def display():
    print("The elements in queue is:")
    for i in queue:
        print(i)
while True:
    print("Select the Operation 1.Add 2.Remove 3.Show 4.Quit")
    choice=int(input("Enter choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Enter correct operation")