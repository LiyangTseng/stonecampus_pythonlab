x = [2,3,4]
# i is element
for i in x:
    print(i,end=" ")
print()
# i is position
for i in range(len(x)):
    print(x[i],end=" ")    
print()
# index & value
for idx, i in enumerate(x):#enumerate = "列舉"
    print(idx+1,i,sep=" : ")
print()


x.append(5)
print(x)
print()


y=[1,2]
# new list, and then copy all elements in x,y
# and assign the reference to variabla z 
z=x+y
print(x,y,z,sep="\n")
print()

z=x # 此行的意義為"z的起始位置與x的起始位置相同"!(python的程式語言中 x=[1,2,3]代表x會儲存x的起始位置)
z[0]=99
print(x,z,sep="\n")

x.append(y)
print(x)
print()

print(len(x))
print(x[len(x)-1])
print(x[-1])
print(x)
x[2:3]=[90,91,92]
print(x)
x[2:4]=[90,91,92]
