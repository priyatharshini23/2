num=int(input("Enter any number:"))
p=list(map(int,str(num)))
q=list(map(lambda x:x**3,p))
if(sum(q)=num):
    print("Yes")
else:
    print("No")
