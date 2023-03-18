from typing import List, Dict, Optional

from pydantic import BaseModel


class Error(BaseModel):
    msg: str
    code: Optional[int]


class GenericResponse(BaseModel):
    msg: str = ""
    errors: List[Error] = []
    success: bool = True


class ChatLogEntryRequest(BaseModel):
    message: str
    timestamp: int
    is_sent: bool


class ChatLogEntryResponse(BaseModel):
    message_id: str


class DataResponse(BaseModel):
    data: List[Dict] = []
