import getpass

def change_password(username, current_password, new_password, password_file="passwd.txt"):
    with open(password_file, "r") as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        if line.startswith(f"{username}:"):
            _, _, current_stored_password = line.split(":")
            if current_stored_password.strip() == current_password:
                lines[i] = f"{username}:{current_stored_password}:{new_password}\n"
                with open(password_file, "w") as file:
                    file.writelines(lines)
                print("Password changed.")
                return
            else:
                print("Current Password is invalid.")
                return
    
    print("Username not found.")

if __name__ == "__main__":
    username = input("User: ")
    current_password = getpass.getpass("Current Password: ")
    new_password = getpass.getpass("New Password: ")
    confirm_password = getpass.getpass("Confirm: ")

    if new_password == confirm_password:
        change_password(username, current_password, new_password)
    else:
        print("Passwords do not match.")
