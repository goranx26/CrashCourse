import json


def get_stored_username():
    """Get the stored username if available"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
           username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    """Prompt for and store a new username"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    """Greet the user by name."""
    username = get_stored_username()

    if username:
        correct = input("Is this you? Username: " + username + "\nY/N\n")
        while True:
            if correct.lower() == 'y':
                print('Welcome back ' + username + '!')
                break
            elif correct.lower() == 'n':
                get_new_username()
                print("We will remember you when you get back " + username + '!')
                break
            else:
                correct = input('Please type y or n.')


    else:
        username = get_new_username()
        print("We will remember you when you get back " + username + '!')



greet_user()
