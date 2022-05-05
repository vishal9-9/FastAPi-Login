from jose import JWTError, jwt
from schemas import TokenData


SECRET_KEY = "8c7c0b71524e5d89a01ee7345b8b065dad4bf69c3bceabd24f251271d90cfe6c"

def create_access_token(data: dict):
    to_encode = data.copy()
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)
    return encoded_jwt

def verify_token(tokens:str,credentials_exception):
    try:
        payload = jwt.decode(tokens,SECRET_KEY)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = TokenData(email = email)
    except JWTError:
        raise credentials_exception