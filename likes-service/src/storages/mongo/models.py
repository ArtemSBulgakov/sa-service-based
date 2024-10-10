from beanie import PydanticObjectId
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


class LikeSchema(BaseModel):
    message_id: PydanticObjectId
    username: str


class Like(LikeSchema, CustomDocument):
    pass


document_models = [User, Message, Like]
