student = {}

def test():
    num = int(input())
    print(num)
    for i in range (0,num):
        line = input()
        # print(line)
        tokens = line.split()
        # print(tokens)
        college = tokens[0]
        
        for j in range(1,5):    
           student[tokens[0] + "-" + str(j) ] = int(tokens[j])
        '''
        for j in range (1,):
            if int(tokens[j]) != 0:
                student[tokens[0] + "-" + str(j) ] = int(tokens[j])
        '''
          
    #print(student)
    num = int(input())
    print(num)
    for i in range(0,num):
        line = input()
        # print(line,student[line])#用student[] 若沒有值 程式會中斷 
        print(line,student.get(line))#用get時，若沒有值，會回傳none
test()