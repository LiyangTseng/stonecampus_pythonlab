import sys

birthday = {}

def test():
    for line in sys.stdin:
        line = line.strip()
        #print(line)
        tokens = line.split()
        print(tokens)
        m = int(tokens[1])
        if birthday.get(m):       #if birthday.get(m) exist
            birthday[m] += 1
        else:
            birthday[m] = 1
    #print(birthday)
    for i in range(1,13):
        print(i, birthday.get(i))    

test()