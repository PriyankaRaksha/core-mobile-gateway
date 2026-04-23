def authenticate_request(token):
    if not token:
        raise Exception("Missing token")

    user = decode(token)
    return user