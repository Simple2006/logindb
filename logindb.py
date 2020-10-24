import sys, hashlib

class loginData:
    def __init__(self, name, bday, email, username, password):
        self.name = name
        self.bday = bday
        self.email = email
        self.username = username
        self.password = password

def register():
    name1 = input("Enter your name: ")
    bday1 = input("Enter your birthdate (mm/dd/yyyy): ")
    email1 = input("Enter your email: ")
    username1 = input("Enter your username: ")
    password1 = input("Enter your password: ")
    info1 = loginData(name1, bday1, email1, username1, password1)
    lusername = hashlib.md5(info1.username.encode())
    lpassword = hashlib.md5(info1.password.encode())
    info1.username = lusername.hexdigest()
    info1.password = lpassword.hexdigest()
    extrainfo = open("extrainfo.txt", "a")
    extrainfo.write(f"Name: {info1.name}\nBirthday: {info1.bday}\nEmail: {info1.email}\n")
    if len(info1.password) < 8:
        print("Password too short!")
    if len(info1.password) >= 8:
        user = open("usernames.txt", "r")
        userC = user.readlines()
        for line in userC:
            if info1.username == line.strip():
                print("Username taken!")
                sys.exit()
        user = open("usernames.txt", "a")
        user.write(info1.username + "\n")
        user.close()
        passw = open("passwords.txt", "a")
        passw.write(info1.password + "\n")        
        passw.close()
        cont = input("Proceed to login? | Y or N: ")
        if cont.lower() == "y":
            loginAcc()
        if cont.lower() == "n":
            sys.exit()

def loginAcc():
    usercheck = input("Enter your username: ")
    lusercheck = hashlib.md5(usercheck.encode())
    usercheck = lusercheck.hexdigest()
    user = open("usernames.txt", "r")
    checkuserC = user.readlines()
    for line in checkuserC:
        if usercheck != line.strip():
            print("User not found")
        elif usercheck == line.strip():
            user.close()
            passcheck = input("Enter your password: ")
            lpasscheck = hashlib.md5(usercheck.encode())
            passcheck = lpasscheck.hexdigest()
            passw = open("passwords.txt", "r")
            checkpassC = passw.readlines()
            for line in checkpassC:
                if passcheck != line.strip():
                    print("Password incorrect")
                    sys.exit()
                elif passcheck == line.strip():
                    passw.close()
                    print("Logging In...")
                    return

reglog = input("Login or Register | L or R: ")
if reglog.lower() == "r":
    register()
if reglog.lower() == "l":
    loginAcc()