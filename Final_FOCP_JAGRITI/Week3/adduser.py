import getpass

def add_user(username, real_name, password, password_file="passwd.txt"):
    with open(password_file, "a") as file:
        file.write(f"{username}:{real_name}:{password}\n")
    print("User Created.")

if __name__ == "__main__":
    username = input("Enter new username: ")
    real_name = input("Enter real name: ")
    password = getpass.getpass("Enter password: ")
    
    # Check if the username already exists
with open(r"C:\Users\DELL\Desktop\Week3\passwd.txt", "r+") as file:
    existing_usernames = [line.split(":")[0] for line in file.readlines()]

    if username in existing_usernames:
        print("Cannot add. Most likely username already exists.")
    else:
        add_user(username, real_name, password)
