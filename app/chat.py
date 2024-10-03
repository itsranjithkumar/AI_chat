# app/routers/chat.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .module import ChatMessageDB  # Import your ChatMessageDB model
from .schemas import ChatMessage  # Import your ChatMessage schema
from .security import get_current_user  # Import your authentication dependency
from .db import save_message_to_db  # Import your database function
import openai

router = APIRouter()

@router.post("/chat")
async def get_chat_response(message: ChatMessage, user = Depends(get_current_user)):
    # Process the chat message and get a response from OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=message.message,
        max_tokens=150,
    )
    # Save the message and response to the database
    save_message_to_db(message=message.message, response=response.choices[0].text.strip())
    
    return {"response": response.choices[0].text.strip()}
