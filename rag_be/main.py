import http
import uvicorn
from fastapi import FastAPI, Path

from query_qa import execute
from controllers import session_controller, user_controller
app = FastAPI()
app.title = 'RAG App'
app.version = "0.0.1"

app.include_router(session_controller.session_router)
app.include_router(user_controller.user_router)


@app.get('/search/{user_query}', status_code=http.HTTPStatus.OK)
async def search(user_query: str = Path()):
    response = await execute(user_query)
    return {'data': response}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)