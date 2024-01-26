def delete_user(username, password_file="passwd.txt"):
    with open(password_file, "r") as file:
        lines = file.readlines()

    with open(password_file, "w") as file:
        for line in lines:
            if not line.startswith(f"{username}:"):
                file.write(line)
    
    print("User Deleted.")

if __name__ == "__main__":
    username = input("Enter username: ")
    delete_user(username)
