inFile = open("dogs.txt", "r")
lines = []
for line in inFile:
   strLine = line.strip().split(' ')
   strLine = (strLine[1] + " " + strLine[0])
   lines.append(strLine)
a = '\n'.join(sorted(lines,key= lambda lines:lines[0]))
print(a)