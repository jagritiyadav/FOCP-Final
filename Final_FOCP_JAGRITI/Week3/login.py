import getpass

def login(username, password, password_file="passwd.txt"):
    with open(password_file, "r") as file:
        for line in file:
            stored_username, _, stored_password = line.strip().split(":")
            if stored_username == username and stored_password == password:
                print("Access granted.")
                return
        print("Access denied.")

if __name__ == "__main__":
    username = input("User: ")
    password = getpass.getpass("Password: ")
    login(username, password)
