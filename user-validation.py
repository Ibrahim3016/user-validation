import random
import string

# create empty users dictionary and update for each complete new user entry
users = {}
# create empty new_user list to store each user details
new_user = []

# Check if a new user will be added 
while True:
    add_user = input("Do you want to add a new user? [y/n]: ")
    if add_user == "y":
        username = input('Enter your username: ')
        
        # check if username already exists and prompt for another one
        while username in users:
            username = input("Username already exist. Please enter another username: ")
        
        # collect user details
        f_name = input('Enter your first name: ')
        l_name = input('Enter your last name: ')
        email = input('Enter your email address: ')


        # Generate random string of length 5
        def randomString(stringLength=5):
            password_characters = string.ascii_letters + string.digits + string.punctuation
            return ''.join(random.choice(password_characters) for i in range(stringLength))


        generated_password = randomString()

        # create password with first two letter of first name, random string and last 2 letters of last name
        password = f_name[:2] + generated_password + l_name[-2:]

        # create user
        user = [f_name, l_name, email, password]

        # check if user is satisfied with the password and display the full user details
        print("Are you satisfies with the password:", password, "[y/n]:")
        satisfied = input()
        if satisfied == "y":
            new_user = ("First name:", user[0], "Last name:", user[1], "Email:", user[2], "Password:", user[3])
            print(username, "details:", new_user)
        elif satisfied == "n":
            password = input("Enter your preferred password, at least 7 characters long: ")
            while len(password) < 7:
                print("Password is too short. It must be 7 characters long")
                password = input()
            else:
                new_user = [("First name:", user[0], "Last name:", user[1], "Email:", user[2], "Password:", user[3])]
                print(username, "details:", new_user)
            pass
        
        # attach username as the key and new_user as the value in users dictionary and update
        key, value = username, new_user
        users.update({key: value})
    
    # if no other users will be added, print the content of users dictionary
    elif add_user == "n":
        print(users)
        break
