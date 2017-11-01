def breakdown(li):
    result = []
    for i in range(len(li)-1, -1, -1):
        result.append(li[:i+1])
    return result

a = [3, 7, 1, 5, 4, 2, 8, 6]
my_lists = breakdown(a)
print(my_lists)

a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
my_lists = breakdown(a)
print(my_lists)



if __name__ == '__main__':
    breakdown([3, 7, 1, 5, 4, 2, 8, 6])



# def breakdown(maximum):
#     result = [] 
#     for i in range():

# if __name__ == '__main__':
#     breakdown(maximum)

