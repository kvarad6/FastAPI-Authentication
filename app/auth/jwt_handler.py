# This file is responsible for signing , encoding , decoding and returning JWTS

# Time is module will be responsible for setting an expiration limit of tokens
import time

# jwt module is responsibke for encoding and decoding generated token strings
import jwt

# decouple helps to organise settings so that you can change paramaters without having to redeploy application.
# also makes it easy to store parameters in ini/.env file.
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# function to return generated tokens (JWTs)
def tokenResponse(token: str):
    return {
        "access token": token
    }


# function to sign the jwt strings
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time()+600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return tokenResponse(token)


# function to decode jwt
def decodeJWT(token: str):
    try:
        decodeToken = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decodeToken if decodeToken['expires'] > time.time() else None
    except:
        return {}
