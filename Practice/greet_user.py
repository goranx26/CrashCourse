import json

filename = 'username.json'
with open(filename, encoding='UTF-8') as f_obj:
    username = json.load(f_obj)
    print('Welcome back ' + username + "!")
