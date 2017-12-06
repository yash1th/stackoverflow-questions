from itertools import izip

list1 = [['A','B','C',4,'D'],['A','B','C',9,'D'],['A','B','C',5,'D'],['A','B','C',6,'D'],['A','B','C',7,'D']]
list2 = [[1,2,3,2,5],[1,2,3,5,5],[1,2,3,3,5],[1,2,3,4,5],[1,2,3,1,5],[1,2,3,2,5]]

for i in izip(list1,list2):
	for item1, item2 in izip(i[0],i[1]):
		if item1 == item2:
			print item1


from itertools import izip

list1 = [['A','B','C',4,'D'],['A','B','C',9,'D'],['A','B','C',5,'D'],['A','B','C',6,'D'],['A','B','C',7,'D']]
list2 = [[1,2,3,2,5],[1,2,3,5,5],[1,2,3,3,5],[1,2,3,4,5],[1,2,3,1,5],[1,2,3,2,5]]

for item1 in list1:
	for item2 in list2:
		for i,j in izip(item1, item2):
			if i==j:
				print i

		# for i in range(len(item1)):
		# 		if item1[i] == item2[i]:
		# 			print item1[i]


                