# import csv

# with open("Details.csv","a+") as Details:
#     w=csv.writer(Details,delimiter=",")

#     headers1=["Name","Age","Year Group"]
#     line=Details.readlines()
#     if line!=["Name","Age","Year Group"]:
#         w.writerow(headers1)
#     print("Welcome User, to my Topics Quiz!\n---------------------------------------\nYou can choose from 3 different topics:\n  • History\n  •Music\n •  Computer Science\n---------------------------------------")
#     print("Before we start, we need to register an account.")
#     User=input("Enter your name:\n")
#     Age=input("Enter your age:\n")
#     Year=input("Enter your year group:\n")

#     details=[User,Age,Year]
#     w.writerow(details)
#     Details.close()

# with open("UserPass.csv","a+") as Userpass:
#     w=csv.writer(Userpass,delimiter=",")
#     headers2=["Username","Password"]
#     if headers2 not in Userpass:
#        w.writerow(headers2)

# NewUser=(User[:3]+Age)
# print("Great! Your username is set to: {}".format(NewUser))
# Pass=input("Enter a password for your account:\n")
# userpass = [NewUser,Pass]
# import os
# file_exists = os.path.isfile(os.getcwd()+'/UserPass.csv')
# print(file_exists)
# import sys
# sys.exit()
# with open("UserPass.csv","a+") as Userpass:
#     w = csv.writer(Userpass, delimiter = ',')
#     headers2=["Username","Password"]
#     if not file_exists:
#         w.writerow(headers2)
#     w.writerow(userpass)

testDict = {0:{12:[(1,5),[23,1]],1:[(2,4),[23,1]],2:[(1,2),[1]]}}

 for k,v in testDict.items():
    for k2, v2 in v.items(): 
       yvalue = v2[0][1]

       if v2[1] == [23,1] :

         yvalue.remove(1)