from fastapi import APIRouter

router = APIRouter()

@router.get("/comments")
async def comments():
    return {"message": "Hello this is comments router"}