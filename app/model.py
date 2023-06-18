from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id: int = Field(default=None)
    title: str = Field(default=None)
    content: str = Field(default=None)

    class Config:
        schema_extra = {
            "post_demo": {
                "title": "Some title about animals",
                "content": "Some content about animals"
            }
        }


# schemas to handle registration and login
class userSchema(BaseModel):
    fullName: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema = {
            "userDemo": {
                "name": "varad",
                "email": "abc@123.com",
                "password": "abc123"
            }
        }


class userLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        schema = {
            "userDemo": {
                "email": "abc@123.com",
                "password": "abc123"
            }
        }
