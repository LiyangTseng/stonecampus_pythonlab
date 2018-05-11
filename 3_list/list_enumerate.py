def prList(arr):
    for idx,el in enumerate(arr):
        if(idx!=len(arr)-1):
            print(el,end=" , ")
        else:
            print(el)
    
a = [10,20,30,40,50]
b = [30,4,56] 
prList(a)
prList(b)


def enumList(arr):
    for idx,el in enumerate(arr):
        print(idx+1,". ",el)
     
     
enumList(['apple', 'orange', 'banana'])
'''
1. apple
2. orange
3. banana
'''
