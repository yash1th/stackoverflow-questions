print ("Welcome to my Quiz!")
existing = input("Are you an existing user?: ")
if existing.lower == "yes":
    print("Enter your credidentials")
username= input("Enter your Username: ")
password= input("Enter your Password: ")
file= open("data.txt", "r")
found=False
for line in file:
    account = line.split(",")
    if account[0] == username:
        password= existing[1]
        found=True
file.close()
if found==True:
    print("Welcome Back", username ,)
if found==False:
    print("Account not found")
else:
    existing.lower == "no"
    user= input("Enter your first name: ")
    year= input("Enter the year you are in: ")
    password= input("Enter your password: ")
    username=user[:2]+year
    writefile=open("data.txt","a")
    writefile.write(username + "," + password + "\n")
    writefile.close()
    print("Your account has been created." "Your username is..", username , "..and your password is", password,)
