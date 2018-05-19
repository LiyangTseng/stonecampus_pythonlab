#print("Hello World")
#print("Hello","World",sep="----")
#print("Hello","World",sep="\n")

#s = "hello"
#print(s)
#print(str(s))
#t = 123
#print(t+1)
#print(str(t)+"1")
#print('hello %s %d' % ("Bob", 123))

#def test(a=2,b=5,c=9):
#    print(a,b,c,sep=" ")
#test()

#import sys
#def readInput():
#        print(line.strip())
#readInput()

'''
for x in range(0,5):
    print(x,end="__")
print("\n")
for x in range(0,5,1):
    print(x,end="__")
print("\n")
for x in range(0,5,2):
    print(x,end="__")
print("\n")
'''
'''
a=['0x','1x','2x','3x','4x','5x','6x','7x']
for i,item in enumerate(a):
    print(i,item)
    #print(i)
    #print(item)
'''
#a=[0,1,2,3]
#print([x ** 3 for x in a])

#nums = [0, 1, 2, 3, 4]
#squares = [x ** 2 for x in nums]
#print("Example 1"squares) # prints [0, 1, 4, 9, 16]

listone = [2, 3, 4] 
listtwo = [2*i for i in listone if i > 2] 
print(listtwo)