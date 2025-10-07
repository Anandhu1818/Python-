num=[]
n=int(input("Enter the element:"))
print("enter the list of integers:")
for i in range(1,n+1):
      e=int(input())
      if(e>100):
            num.append("over")
      else:
            num.append(e)
print("entered list.",num)
            
