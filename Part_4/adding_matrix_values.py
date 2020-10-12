m1 = [[35,12,6],[-32,5,-26],[10,8,-1]]
m2 = [[-31,29,34],[12,11,-25],[28,21,-42]]

def matrixadd (m1,m2):
    m3 = []
    check = True
    if len(m1)!=len(m2):
        check = False
    else:
        for i in range(len(m1)):
            if len(m1[i]) != len(m2[i]):
                check = False
    if check:
        for i in range(len(m1)):
            c = []
            for j in range(i):
                print(m1[i][j])
    else:
        print ("matrix is no the same")








    # return m3
matrixadd(m1,m2)