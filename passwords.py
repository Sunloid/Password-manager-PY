#Program to Manage passwords 

master_pwd = input("Enter the Master password: ")
master_pwd = master_pwd.rstrip()



def add():
    user = input("Username: ")
    user = user.rstrip()
    pwd = input("Password: ")
    with open ("passwords.txt","a") as yes:
        yes.write("Username: "+ user + " | "+"Password: " + pwd + "\n")

def view():
    with open ("passwords.txt","r") as yes:
        for line in yes.readlines():
            data = line.rstrip()
            username , password = data.split("|")
            print("Username: "+ username+ "| " "Password: "+ password)

while True:
    mode = input("What would you like to do with your passwords: ( 'view', 'add' ), Press q to quit  ")
    mode = mode.rstrip()
    if mode == "q": 
        break
    if mode == "view":
        view() 
    elif mode == "add":
        add()
    else: 
        print("Invalid input.")
        continue