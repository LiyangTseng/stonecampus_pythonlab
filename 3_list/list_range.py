num=range(5,0,-1)
print(num)

num=list(range(5,0,-1))
print(num)

a=[1,2,3]
total=0
for el in a:
    total+=el
total2=sum(a)

print(total,total2)

b = range(5,0,-1)
total3 = sum(b)
print(total3)

strA = "stone"
'''
    strA[0]="Y"
    print(strA)
'''
strA = list(strA)
strA[0] = "Y"
print(strA)
# join on apply for