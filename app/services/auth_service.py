def authenticate_request(token):
    user = decode(token)

    if user.get("exp") < now():
        raise Exception("Token expired")

    return user

def refresh_token(user):
    token = generate_jwt(user)

    return {
        "token": token,
        "expires_in": 3600
    }

def get_user_permissions(user):
    return permissions.get(user["role"], [])

def logout_user(user_id):
    session_key = f"session:{user_id}"

    if cache.exists(session_key):
        cache.delete(session_key)

    return {"status": "logged_out"}