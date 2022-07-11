import json


def check_email(email, all_users_data):
    for user in all_users_data:
        if email == user['Email']:
            return True
    return False


# functions which used for adding users to user.json
def user_add():
    # try:
    user = {
        "first_name": input("First Name: "),
        "last_name": input("Last Name: "),
        "Email": input("Email: "),
    }
    # except:

    for v, k in user.items():
        if len(k) == 0:
            raise Exception("incorrect data")
    try:
        file = open('users.json', 'r')
        all_users_data_json = file.read()
        all_users_data = json.loads(all_users_data_json)
        file.close()
        if len(all_users_data) > 0:
            user['id'] = all_users_data[-1]['id'] + 1
        else:
            user['id'] = 1
        if not check_email(user['Email'], all_users_data):
            all_users_data.append(user)
            with open('users.json', 'w') as file:
                file.write(json.dumps(all_users_data))
        else:
            print("User with this email already exist!!!")
    except FileNotFoundError:
        print("file not found")




# except ValueError:
#     print("incorrect data")
# except FileNotFoundError:
#     print("file not found")


def get_all():
    try:
        with open('users.json', 'r') as file:
            users = json.loads(file.read())
        for user in users:
            print("User #" + str(user['id']))
            print("First Name: " + user['first_name'])
            print("Last Name: " + user['last_name'])
            print("Email: " + user['Email'])
    except FileNotFoundError:
        print("file not found")


def search_by(search_str, what_to_search):
    try:
        with open('users.json', 'r') as file:
            users = json.loads(file.read())
    except FileNotFoundError:
        print("file not found")
    else:
        for user in users:
            if str(user[what_to_search]).lower() == str(search_str).lower():
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['Email'])


def update_user():
    try:
        file = open('users.json', 'r')
        users = json.loads(file.read())
        file.close()
        id = int(input("Type id of user which you want to update: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        for user in users:
            if user['id'] == id:
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['Email'] = email
        with open('users.json', 'w') as file:
            file.write(json.dumps(users))
    except ValueError:
        print("please input correct data")
    except FileNotFoundError:
        print("file nit found")
