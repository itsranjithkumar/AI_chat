from pydantic import BaseModel
from typing import Optional



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str

class UserInDB(User):
    hashed_password: str

class LoginData(BaseModel):
    username: str
    password: str


class ChatMessage(BaseModel):
    message: str
