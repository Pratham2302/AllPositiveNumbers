list1=[]
x=int(input("Enter the size of the elements:"))
for i in range(0,x):
    z=int(input())
    list1.append(z)
list2=[]
y=int(input("enter the size of the elements:"))
for i in range(0,y):
    k=int(input())
    list2.append(k)
print("input:list1=" + str(list1))
print("output: ",end=" ")
for num in list1:
    if(num>0):
        print(str(num)+",",end=" ")
    else:
        continue
print("\ninput:list2=:" + str(list2))
print("output:",end=" ")
print("[",end=" ")
for num in list2:
    if(num>0):
        print(str(num)+",",end=" ")
    else:
        continue
print("]",end=" ")

