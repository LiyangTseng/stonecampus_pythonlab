def result(answer,guess):
    A=0
    B=0
    for idx_ans, val_ans in enumerate(answer):
        for idx_gus, val_gus in enumerate(guess):
            #print(idx_ans, val_ans, idx_gus, val_gus)
            if val_ans == val_gus:
                if idx_ans == idx_gus:
                    A+=1
                else:
                    B+=1 

    return str(A)+"A"+str(B)+"B"

print(result('1234','4321'))
print(result('4657','9658'))
print(result('9876','6879'))