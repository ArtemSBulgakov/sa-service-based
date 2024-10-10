from fastapi import APIRouter

from src.storages.mongo.models import User, Message

router = APIRouter(tags=["Messages"])

@router.post(
    "/create_post",
    responses={200: {"description": "Message info"}},
)
async def post_message(username: str, message: str) -> Message | None:
    """
    Create a new message
    """
    user = await User.find_one(User.username == username)
    if user is None:
        return None
    message = await Message(message=message, username=username).create()
    return message


@router.get(
    "/read_feed",
    responses={200: {"description": "Last 10 messages"}},
)
async def feed() -> list[Message]:
    """
    Show last 10 messages
    """
    messages = await Message.find().sort((Message.id, -1)).limit(10).to_list()
    return messages
