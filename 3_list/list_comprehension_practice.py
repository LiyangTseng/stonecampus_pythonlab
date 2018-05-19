'''
squareList(nums): 回傳一個 list, 其中的元素為 nums 中每個數字的平方, 
例如: squareList([3, 4, 5]) 回傳 [9, 16, 25]
'''

def squareList(nums):
    square = []
    print([x ** 2 for x in nums ])
'''
absList(nums, x): 回傳一個 list, 其中的元素為 nums 中絕對值小於 x 的數字,
例如: absList([3, 4, -1, -2, 2, 7, 1], 3) 回傳 [-1, -2, 2, 1]
'''
def absList(nums, x):
    print([y for y in nums if abs(y) < x ])



'''
piList(n): 回傳一個 list, 其中的元素為從小數第 1 位到第 n 位的 pi 值, 
例如 : piList(5) 回傳 [3.1, 3.14, 3.142, 3.1416, 3.14159]
'''
from math import pi
def piList(n):
    print([str(round(pi,i)) for i in range(1,n+1)])



def test():
    #nums = [3,4,5]
    #squareList(nums)
    #absList([3, 4, -1, -2, 2, 7, 1], 3)
    piList(5)

test()