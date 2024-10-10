from beanie import PydanticObjectId
from fastapi import APIRouter

from src.storages.mongo.models import User, Like

router = APIRouter(tags=["Likes"])

@router.post(
    "/like_message",
    responses={200: {"description": "Like record"}},
)
async def like_message(username: str, message_id: PydanticObjectId) -> Like | None:
    """
    Set like for message
    """
    user = await User.find_one(User.username == username)
    if user is None:
        return None
    like = await Like.find_one(Like.username == username, Like.message_id == message_id)
    if like is not None:
        return like
    like = await Like(username=username, message_id=message_id).create()
    return like


@router.post(
    "/unlike_message",
    responses={200: {"description": "Success"}},
)
async def unlike_message(username: str, message_id: PydanticObjectId) -> bool:
    """
    Remove like from message
    """
    user = await User.find_one(User.username == username)
    if user is None:
        return False
    like = await Like.find_one(Like.username == username, Like.message_id == message_id)
    if like is None:
        return False
    await like.delete()
    return True



@router.get(
    "/message_likes",
    responses={200: {"description": "Likes for message"}},
)
async def read_message_likes(message_id: PydanticObjectId) -> list[Like]:
    """
    Get likes for message
    """
    likes = await Like.find(Like.message_id == message_id).to_list()
    return likes
