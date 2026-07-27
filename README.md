FastAPI Real-Time Chat Application
Overview

This is a simple real-time chat application built using FastAPI and WebSockets. Users can enter a username, join a chat room, and exchange messages instantly with other users in the same room.

Features

1. Real-time messaging using WebSockets
2. Multiple chat rooms
3. Username support
4. Message timestamps
5. Coloured usernames

FastAPI backend
Jinja2 templates
HTML, CSS, and JavaScript frontend
Technologies Used
Python
FastAPI
WebSockets
Jinja2
HTML
CSS
JavaScript
Project Structure
python_chat_room/
│
├── templates/
│ ├── index.html
│ └── chat.html
│
├── static/
├── app.py
├── manager.py
├── requirements.txt
└── README.md
Installation

- Clone the repository.
- Create a virtual environment.
- Install the required packages.
- pip install -r requirements.txt
  Run the application.
  python -m uvicorn app:app --reload

Open your browser and visit:
http://127.0.0.1:8000

How to Use
Enter a username.
Enter a room name.
Click Join Room.
Start chatting with anyone in the same room.
Future Improvements
User authentication
Chat history with a database
Emojis
File sharing
Online user list
Author

Sanjai

Built as a learning project using FastAPI and WebSockets.
