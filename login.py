# Simple login and registration program

# Dictionary to store user credentials
users = {}

# Function to register a new user
def register():
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists! Please try a different username.")
    else:
        password = input("Enter a new password: ")
        pas=input("confirm your password")
        if password==pas:
          users[username] = password
          print("Registration sucessfull")
        else:
            print("password didnt match set again")
            return 0

# Function to log in an existing user
def login():
    username = input("Enter your username: ")
    if username in users:
        password = input("Enter your password: ")
        if users[username] == password:
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Username does not exist. Please register first.")

# Main menu function
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Register")
        print("2. Login")
        print("3. log out")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            print("visit again . Goodbye!")
            break
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

# Run the menu function
menu()
