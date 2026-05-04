def authenticate_request(token):
    user = decode(token)

    if user.get("exp") < now():
        raise Exception("Token expired")

    return user

