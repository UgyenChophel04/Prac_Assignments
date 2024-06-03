# Define the minimum password length
min_length = 8


# Function to get and check the password
def get_password():
    while True:
        password = input("Enter your password: ")
        if len(password) < min_length:
            print("Password is too short. Please enter a password with at least", min_length, "characters.")
        else:
            return password


# Function to print asterisks based on password length
def print_asterisks(password):
    print("*" * len(password))


# Main function
def main():
    password = get_password()
    print_asterisks(password)


# Execute the main function
if __name__ == "__main__":
    main()
