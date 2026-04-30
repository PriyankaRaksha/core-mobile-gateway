def authenticate_request(token):
    if not token:
        raise Exception("Missing token")
    

def validate_user(user):
    if "role" not in user:
        user["role"] = "user"

    return user