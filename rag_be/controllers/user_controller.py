import http
from fastapi import APIRouter, Body, File, UploadFile, Query

from models.base import GenericResponseModel
from models.user_model import CreatedUserModel

from services.user_service import UserService

user_router = APIRouter(prefix="/apis/user", tags=["CRUD_user"])

# Get all user
@user_router.get('/',status_code=http.HTTPStatus.OK, response_model=GenericResponseModel)
async def get_all_user():
    response = await UserService.get_all_user()
    return response

# Get user by id
@user_router.get('/{user_id}',status_code=http.HTTPStatus.OK, response_model=GenericResponseModel)
async def get_user(user_id: str):
    response = await UserService.get_user(user_id=user_id)
    return response

# Create user
@user_router.post('/',status_code=http.HTTPStatus.CREATED, response_model_by_alias=False)
async def create_user(user_data: CreatedUserModel):
    user_data = user_data.model_dump()
    response = await UserService.create_user(data=user_data)
    return response

# # Update user
# @user_router.post('/{user_id}',status_code=http.HTTPStatus.CREATED, response_model_by_alias=False)
# async def update_user(user_data: CreatedUserModel):
#     response = await UserService.update_user(data=user_data)
#     return response

# Delete user by id
@user_router.delete('/{user_id}',status_code=http.HTTPStatus.OK, response_model=GenericResponseModel)
async def delete_user(user_id: str):
    response = await UserService.delete_user(user_id=user_id)
    return response
