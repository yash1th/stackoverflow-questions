def sum(m,n):
    result = 0
    m1 = 1/m
    n1 = 1/n
    while range(m1,n1):
        result= sum(x for x in range(m1,n1))
    return result