print("Hello World")
print("Hello", "World")
print("Hello", "World", sep="-")
print("Hello", "World", sep="%")
print("Hello", "World", sep="*", end="2")
print("HELLO")

a=1 
b=2

str1= "I am learning programming."
print(str1)

print(len(str1))
print(str1[2])
print(str1[5:13])
print(str1[:4])
print(str1[14:])
print(str1[::-1])

print("{0} {1}".format(100,200))
print("num1: {0} num2: {1}".format(a,b))
print("{0:10}{1:10}".format(200,300))
print("{0:<7}{1:<7}{2:<7}".format(12345,  456,  9998))
print("{0:>7}{1:>7}{2:>7}".format(12345,  456,  9998))

#請定義一個字串 str = "Stone Campus", 請印出以下內容:
s = "Stone Campus"

#這個字串的長度
print(len(s))
#位置 6 的字母 (使用 [])
#從位置 3 到 9 的子字串 "ne Camp" (使用util.slice())
#從位置 3 到 最後的子字串 "ne Campus" (使用util.slice())
#從位置 0 到 9 的子字串 "Stone Camp"  (使用util.slice())