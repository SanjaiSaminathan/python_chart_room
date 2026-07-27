from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Form
from fastapi import WebSocket

from manager import ConnectionManager

app = FastAPI()

manager = ConnectionManager()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.post("/chat", response_class=HTMLResponse)
def join_chat(
    request: Request,
    username: str = Form(...),
    room: str = Form(...)
):
    return templates.TemplateResponse(
        request=request,
        name="chat.html",
        context={
            "username": username,
            "room": room
        }
    )


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):

    await manager.connect(websocket)

    try:
        while True:

            message = await websocket.receive_text()

            await manager.broadcast(message)

    except:
        manager.disconnect(websocket)