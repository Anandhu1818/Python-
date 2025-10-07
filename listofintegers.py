list1=[]
list2=[]
m=int(input("Enter The Limit Of List1:"))
print("Enter The Elements:")
for i in range(0,m):
    value=int(input())
    list1.append(value)
n=int(input("Enter The Limit Of List2:"))
print("Enter The Elements:")
for i in range(0,n):
    value=int(input())
    list2.append(value)
print(list1,list2)
if len(list1)==len(list2):
    print("Both list1 and list2 are of same length")
else:
    print("Both list1 and list2 are not of same length")
if sum(list1)==sum(list2):
    print("Sum of both list1 and list2 are same")
else:
    print("sum of both list1 and list2 are not same")
list3=[each for each in list1 if each in list2]
print("same members are:",list3)
