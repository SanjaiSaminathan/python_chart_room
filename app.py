from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import Form
from fastapi import WebSocket
from fastapi import WebSocketDisconnect

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
            "request": request,
            "username": username,
            "room": room
        }
    )


@app.websocket("/ws/{room}")
async def websocket_endpoint(
    websocket: WebSocket,
    room: str
):
    await manager.connect(websocket, room)

    try:
        while True:
            message = await websocket.receive_text()

            await manager.broadcast(message, room)

    except WebSocketDisconnect:
        manager.disconnect(websocket, room)