# array = [1,2,3]
# tuple : 儲存相關的資料
book1 = ("#010", "Stone Programming", 330)
(id1, title1, price1) = book1

book2 = "#025", "Python Programming", 230
id2, title2, price2 = book2
#小括號在tuple可省略

#print(book1)
#print(book1[0],book1[1],book1[2])
#print(id1,title1,price1)

arr = [100,200,300]
'''
for i in range (0,len(arr)):
    print(arr[i])
'''
for idx, val in enumerate(arr):
    print(idx, val)
#其實idx,val是以tuple的形式儲存