from openai import OpenAI
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated
from config import settings

router = APIRouter(
    prefix="/agent",
    tags=['Agent']
)


openai = OpenAI(
    api_key=settings.OPENAI_API_KEY
)


@router.post('/chat')
async def chat_with_gpt(message: str):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": message}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))