# import csv
# filename1 = "sheets2.csv"
# filename2 = "newsheet.csv"

# fields = ['A','B','C','D','E']

# average = 0
# total = 0
# row_count = 1

# with open(filename1,'rU') as csvfile1:
#     csvreader = csv.reader(csvfile1)

#     for col in csvreader:
#         print(col[2])
#         #csvwriter.writerow(['stas'])
#         # if len (col[2])>1:
#         #     print("data in col is", "col[4]")
#         # else:
#         #     print("the data entered is", col[2])
# # average = total/row_count
# # print(average)
# # csvwriter.writerow([aver])

# # csvfile1.close()
# # csvfile2.close()

import csv
filename1 = "sheets2.csv"
filename2 = "newsheet.csv"

fields = ['A','B','C','D','E']

average = 0
total = 0
row_count = 1

with open(filename1,'rU') as csvfile1:
    csvreader = csv.reader(csvfile1)


    with open(filename2,'w') as csvfile2:
        csvwriter = csv.writer(csvfile2)

        for col in csvreader:
            csvwriter.writerow(['stas'])
            if len (col[2])==1:
                print("data in col is", "col[4]")
            else:
                print("the data entered is", float(col[2]))
                total = total + int(col[2])
                row_count += 1
average = total/row_count
print(average)
csvwriter.writerow([aver])

csvfile1.close()
csvfile2.close()