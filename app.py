# import the fastapi library

from fastapi import FastAPI

from fastapi.responses import HTMLResponse

from fastapi.templating import Jinja2Templates

from fastapi import Request


from fastapi import Form

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
