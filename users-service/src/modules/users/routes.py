from fastapi import APIRouter

from src.storages.mongo.models import User

router = APIRouter(tags=["Users"])

@router.get(
    "/info",
    responses={200: {"description": "User info"}},
)
async def get_user(username: str) -> User | None:
    """
    Get user info
    """
    user = await User.find_one(User.username == username)
    return user


@router.post(
    "/register",
    responses={200: {"description": "Create new user"}},
)
async def create_user(username: str) -> User | None:
    """
    Create user with username
    """
    user = await User(username=username).create()
    return user
