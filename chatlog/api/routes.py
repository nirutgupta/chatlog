from typing import Optional

from api.models import ChatLogEntryRequest, ChatLogEntryResponse, DataResponse, GenericResponse
from api import app

from fastapi.responses import JSONResponse
from fastapi import status, HTTPException, Request, Query

from config import Config
from exceptions import MessageNotFoundException
from states.chatlog import Chatlog

config = Config()


class ChatlogManager:
    @staticmethod
    @app.post("/v1/chatlogs/{username}",
              tags=["Chatlog Management"],
              summary="Endpoint to add a chatlog",
              responses={
                  200: {"description": "Successfully registered",
                        "model": ChatLogEntryResponse}
              })
    def add_chatlog_entry(username: str, registration_request: ChatLogEntryRequest, request: Request):
        chatlog_state = Chatlog(username=username)
        chatlog_state.add(registration_request.dict())
        response = ChatLogEntryResponse(message_id=chatlog_state.message_id)
        return JSONResponse(status_code=200, content=response.dict())

    @staticmethod
    @app.get("/v1/chatlogs/{username}",
             tags=["Chatlog Management"],
             summary="Endpoint to get chatlogs",
             responses={
                 200: {"description": "List of all chatlog entries of a user",
                       "model": DataResponse}
             })
    def get_all_chatlogs(username, request: Request,
                         limit: int = Query(default=config.USER_CHATLOG_RETRIEVE_DEFAULT_ROWS_COUNT, ge=0),
                         start: Optional[str] = ""):
        response = DataResponse()
        chatlog_state = Chatlog(username=username)
        try:
            response.data = chatlog_state.get_all(limit=limit, start_message_id=start)
        except MessageNotFoundException as exc:
            raise HTTPException(status_code=404, detail=f"{exc}")
        return JSONResponse(status_code=200, content=response.dict())

    @staticmethod
    @app.delete("/v1/chatlogs/{username}",
                tags=["Chatlog Management"],
                summary="Endpoint to delete chatlogs",
                status_code=status.HTTP_200_OK,
                response_model=GenericResponse)
    def delete_all_chatlogs(username, request: Request):
        response = GenericResponse()
        response.msg = "Deleted successfully!"
        chatlog_state = Chatlog(username=username)
        try:
            chatlog_state.delete_all()
        except MessageNotFoundException as exc:
            raise HTTPException(status_code=404, detail=f"{exc}")
        return JSONResponse(status_code=200, content=response.dict())

    @staticmethod
    @app.delete("/v1/chatlogs/{username}/{message_id}",
                tags=["Chatlog Management"],
                summary="Endpoint to delete chatlog",
                status_code=status.HTTP_200_OK,
                response_model=GenericResponse
                )
    def delete_chatlog(username, message_id, request: Request):
        response = GenericResponse()
        response.msg = "Deleted successfully!"
        chatlog_state = Chatlog(username=username, message_id=message_id)
        try:
            chatlog_state.delete()
        except MessageNotFoundException as exc:
            raise HTTPException(status_code=404, detail=f"{exc}")
        return JSONResponse(status_code=200, content=response.dict())
