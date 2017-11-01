def fun():
    check=6
    loginID=1234
    count=0
    a=[]
    for i in range(2):
        a.append([])
        for j in range(2):
            if count<check:
                a[i].insert(j, loginID)
                count+=1
            else:
                pass
            #print(a)
            #break
    a = [[[k for k in range(6)] for i in range(5)] for j in range(3)]
    for p in a:
        for q in p:
            print(q, end=' ')
        print()
fun()
#for i in b:
    # for j in i:
    #     print(j, end=' ')
    # print()
