from data_adapters.user_adapter import UserAdapter
from models.user_model import UserModel
from models.base import GenericResponseModel
import http

import pytz
from datetime import datetime
from fastapi.encoders import jsonable_encoder

class UserService:
    ERROR_ITEM_NOT_FOUND = "Item not found"

    def __init__(self):
        pass

    @staticmethod
    async def create_user(data):
        username = data['username']
        password = data['password']

        vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
        datetime_VN = datetime.now(vietnam_timezone)
        vietnam_now = datetime_VN.strftime("%Y-%m-%d %H:%M:%S")


        # Create User model
        user_model = UserModel()
        user_model.username = username
        user_model.password = password
        user_model.created_by = 'Admin'
        user_model.created_at = vietnam_now

        # Insert in to database
        user_adapter = UserAdapter()
        mongo_data_insert_dict = jsonable_encoder(user_model)
        new_user = user_adapter.insert_one(mongo_data_insert_dict)
        created_user = user_adapter.find_one({"_id": new_user.inserted_id})

        return GenericResponseModel(status_code=http.HTTPStatus.OK, data=created_user, message="Create user successfully")
    
    # Get user by id
    @staticmethod
    async def get_user(user_id):
        user_adapter = UserAdapter()
        user_data = user_adapter.find_one({"_id": user_id})

        return GenericResponseModel(status_code=http.HTTPStatus.OK, data=user_data, message="Get user by id successfully")

    # Get all users
    @staticmethod
    async def get_all_user():
        user_adapter = UserAdapter()
        all_users = user_adapter.find({})
        return GenericResponseModel(status_code=http.HTTPStatus.OK, data=all_users, message="Get all users successfully")
    
    # Delete user by ID
    @staticmethod
    async def delete_user(user_id):
        user_adapter = UserAdapter()
        user_service = UserService()

        # Check if this user exists
        user_data = user_service.get_user(user_id)
        if user_data is None:
            return GenericResponseModel(status_code=http.HTTPStatus.NOT_FOUND, error="Cannot found this user")
        
        # Delete user by id
        user_adapter.delete_one({"_id": user_id})
        return GenericResponseModel(status_code=http.HTTPStatus.OK, message="Delete user successfully")

