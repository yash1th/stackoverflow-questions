import csv
medal=[]
av=[]
i=0
country=[]
out = open('results.txt','w')
with open('medalData.csv', 'r') as f:
    reader = csv.reader(f,delimiter=',')
    for row in reader:
        if row[1]!='Country':
            medal.append(int(row[3])+int(row[4])+int(row[5]))

            country.append(row[1])
            out.write(row[1])
            average = round(((medal[i]/int(row[2])) * 10000000),3)
            av.append(average)

            if average < 0.672 :
                out.write(", {}, WELL Below Average""\n".format(average))
            elif average >= 0.672 and average <= 1.171:
                out.write(", {}, Below Average""\n".format(average))
            elif average == 1.172:
                out.write(", {}, Average""\n".format(average))
            elif average >= 1.173 and average <= 1.672 :
                out.write(", {}, Above Average""\n".format(average))
            elif average > 1.672:
                out.write(", {}, WELL Above Average""\n".format(average))
            i+=1


out.close()
Higest_loc =av.index(max(av))
lowest_loc =av.index(min(av))
print(country[Higest_loc],"has the Highest Ratio")
print(country[lowest_loc],"has the Lowest Ratio")