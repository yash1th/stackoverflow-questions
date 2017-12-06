def write_avg(out_file):
	L = [['S',34],['A',34],['N',34],['L',34]]
	answer = ''
	for item in L: 
		answer = item[0]+','+str(item[1]) + '\n'
		out_file.write(answer)

f = open('jilebi.txt', 'w')
write_avg(f)
f.close()