import uvicorn
from fastapi import FastAPI, Body
from app.model import PostSchema, userSchema, userLoginSchema
from app.auth.jwt_handler import signJWT

posts = [
    {
        "id": 1,
        "title": "Penguins ",
        "text": "Penguins are a group of aquatic flightless birds."
    },
    {
        "id": 2,
        "title": "Tigers ",
        "text": "Tigers are the largest living cat species and a memeber of the genus panthera."
    },
    {
        "id": 3,
        "title": "Koalas ",
        "text": "Koala is arboreal herbivorous maruspial native to Australia."
    },
]

users = []

app = FastAPI()


# def check_user(data: UserLoginSchema):
#     for user in users:
#         if user.email == data.email and user.password == data.password:
#             return True
#     return False


# route handlers

# testing
@app.get("/", tags=["test"])
def greet():
    return {"hello": "world!."}


# Get Posts
@app.get("/posts", tags=["posts"])
def getPosts():
    return {"data": posts}


@app.get("/posts/{id}", tags=["posts"])
def getSinglePost(id: int):
    if id > len(posts):
        return {
            "error": "No such post with the supplied ID."
        }

    for post in posts:
        if post["id"] == id:
            return {
                "data": post
            }


@app.post("/posts", tags=["posts"])
def addPost(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.dict())
    return {
        "data": "post added."
    }


# route for user signup (create a new user)
@app.post("/user/signup", tags=["user"])
def userSignup(user: userSchema = Body(default=None)):
    users.append(user)
    return signJWT(user.email)


def checkUser(data: userLoginSchema):
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False


@app.post("/user/login", tags=["user"])
def userLogin(user: userLoginSchema = Body(default=None)):
    if checkUser(user):
        return signJWT(user.email)
    else:
        return {
            "Error": "Invalid login details"
        }
