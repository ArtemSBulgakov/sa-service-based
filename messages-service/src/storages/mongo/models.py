from pydantic import BaseModel

from src.storages.mongo.__base__ import CustomDocument


class UserSchema(BaseModel):
    username: str


class User(UserSchema, CustomDocument):
    pass


class MessageSchema(BaseModel):
    message: str
    username: str


class Message(MessageSchema, CustomDocument):
    pass


document_models = [User, Message]
