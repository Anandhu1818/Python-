size=int(input("Enter the size"))
num=[]
for i in range (1,size +1):
    n=int(input("Enter the value"))
    num.append(n)
    
print("List:",num)
print("Positive Numbers:")
for x in num:
    if(x>0):
        print(x)
    
