import requests

database = {
    1: "Alice",
    2: "Bob",
    3: "Charlie",
}


def get_user_from_db(user_id):
    user = database.get(user_id)
    return user


def get_users_from_api():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code == 200:
        return response.json()
    else:
        raise requests.HTTPError
