from random import randrange
cluster0Y = [0,1,0,1]
cluster1Y = [0,1,0,1]
while True:
        random_index = randrange(0,len(cluster0Y+cluster1Y))
        if random_index >= len(cluster0Y):
            random_index = random_index - len(cluster0Y)
        if cluster1Y[random_index]==1:
            print('cluster 1 : ',random_index)
            break
        if cluster0Y[random_index]==1:
            print('cluster 0 : ',random_index)
            break
        print('random index = ',random_index)