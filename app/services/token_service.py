import uuid

def generate_token():
    token = str(uuid.uuid4())
    return token