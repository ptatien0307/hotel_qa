from data_adapters.session_adapter import SessionAdapter
from models.session_model import SessionModel
from models.base import GenericResponseModel

import http
import pytz
from datetime import datetime
from fastapi.encoders import jsonable_encoder

class SessionService:
    ERROR_ITEM_NOT_FOUND = "Item not found"

    def __init__(self):
        pass

    # Create new session with empty history
    @staticmethod
    async def create_session(data):
        user_id = data['user_id']
        history = data['history']

        vietnam_timezone = pytz.timezone('Asia/Ho_Chi_Minh')
        datetime_VN = datetime.now(vietnam_timezone)
        vietnam_now = datetime_VN.strftime("%Y-%m-%d %H:%M:%S")

        # Create Session model
        session_model = SessionModel()
        session_model.user_id = user_id
        session_model.history = history
        session_model.created_by = 'Admin'
        session_model.created_at = vietnam_now

        # Insert session into database
        session_adapter = SessionAdapter()
        mongo_data_insert_dict = jsonable_encoder(session_model)
        new_session = session_adapter.insert_one(mongo_data_insert_dict)
        created_session = session_adapter.find_one({"_id": new_session.inserted_id})
        return GenericResponseModel(status_code=http.HTTPStatus.OK, data=created_session, message="Create session successfully")


    # Update history of a session
    @staticmethod
    async def update_session(session_new_data):
        session_id = session_new_data['session_id']
        session_new_history = session_new_data['history']
        
        session_adapter = SessionAdapter()
        session_service = SessionService()

        # Check if this session exists
        session_data = session_service._get_session_by_id(session_id)
        if session_data is None:
            return GenericResponseModel(status_code=http.HTTPStatus.NOT_FOUND, error="Cannot found this session")
        
        # Update session with new history
        query = {"_id": session_id}
        new_values = {"$set": {
            "history": session_new_history,
        }}
        new_session = session_adapter.update_one(query, new_values)
        updated_session = session_adapter.find_one({"_id": new_session.upserted_id})
        return GenericResponseModel(status_code=http.HTTPStatus.OK, data=updated_session, message="Update session successfully")

    # Get all session
    @staticmethod
    async def get_all_session():
        session_adapter = SessionAdapter()
        all_sessions = session_adapter.find({})
        return GenericResponseModel(status_code=http.HTTPStatus.OK, data=all_sessions, message="Get all sessions by ID successfully")


    def _get_session_by_id(self, session_id):
        session_adapter = SessionAdapter()
        session = session_adapter.find_one({"_id": session_id})
        return session


    # Get session by ID
    @staticmethod
    async def get_session(session_id):
        session_service = SessionService()
        session_data = session_service._get_session_by_id(session_id)
        return GenericResponseModel(status_code=http.HTTPStatus.OK, data=session_data, message="Get session by ID Successfully")

    # Delete session by ID
    @staticmethod
    async def delete_session(session_id):
        session_adapter = SessionAdapter()
        session_service = SessionService()

        # Check if this session exists
        session_data = session_service._get_session_by_id(session_id)
        if session_data is None:
            return GenericResponseModel(status_code=http.HTTPStatus.NOT_FOUND, error="Cannot found this session")
        
        # Delete session by id
        session_adapter.delete_one({"_id": session_id})
        return GenericResponseModel(status_code=http.HTTPStatus.OK, message="Delete session successfully")