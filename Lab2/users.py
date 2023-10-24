import json


def dictUsers():
    users = {}

    for i in range(1, 101):
        username = f"user{i}"
        email = f"user{i}@example.com"
        users[username] = email
    
    return users

def usersToJson(dictUsers):
    usersJson = json.dumps(dictUsers, indent=4)
    return usersJson


