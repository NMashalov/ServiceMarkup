from pydantic import BaseModel

class RegisterRequest(BaseModel):
    telegram_login: str