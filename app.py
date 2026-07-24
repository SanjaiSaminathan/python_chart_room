# import the fastapi library

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from fastapi import Request


from fastapi import Form

# import the websocket library

from fastapi import WebSocket

# create an instance object of the fastAPI class

app = FastAPI()

templates = Jinja2Templates(directory="templates")
# decorator

@app.get("/", response_class=HTMLResponse)


def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )
    
    
@app.post("/chat")
def join_chat(
username:str = Form(...),
room:str = Form(...)
):
    return {
    "username": username,
    "room": room
    }
        
# websocket endpoint for chat room
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()

        await websocket.send_text(
            f"You typed: {message}"
        )
