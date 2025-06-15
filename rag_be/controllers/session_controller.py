import http
from fastapi import APIRouter, Body
from pydantic import BaseModel
from models.base import GenericResponseModel
from models.session_model import UpdatedSessionModel, CreateSessionModel
from services.session_service import SessionService

session_router = APIRouter(prefix="/apis/session", tags=["CRUD_session"])

# Get all session
@session_router.get('/',status_code=http.HTTPStatus.OK, response_model=GenericResponseModel)
async def get_all_session():
    response = await SessionService.get_all_session()
    return response

# Get session by id
@session_router.get('/{session_id}',status_code=http.HTTPStatus.OK, response_model=GenericResponseModel)
async def get_session(session_id: str):
    response = await SessionService.get_session(session_id=session_id)
    return response

# Delete session by id
@session_router.delete('/{session_id}',status_code=http.HTTPStatus.OK, response_model=GenericResponseModel)
async def delete_session(session_id: str):
    response = await SessionService.delete_session(session_id=session_id)
    return response

# Create session


@session_router.post('/', status_code=http.HTTPStatus.CREATED, response_model_by_alias=False)
async def create_session(session_data: CreateSessionModel):
    session_dict = {
        "user_id": session_data.user_id,
        "history": [],
    }
    response = await SessionService.create_session(data=session_dict)
    return response

# Update session
@session_router.post('/{session_id}',status_code=http.HTTPStatus.CREATED, response_model_by_alias=False)
async def update_session(session_data: UpdatedSessionModel):
    session_data = session_data.model_dump()
    response = await SessionService.update_session(session_new_data=session_data)
    return response