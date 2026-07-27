from fastapi import WebSocket


class ConnectionManager:

    def __init__(self):
        # Store connections by room
        self.active_connections = {}

    async def connect(self, websocket: WebSocket, room: str):
        await websocket.accept()

        # Create the room if it doesn't exist
        if room not in self.active_connections:
            self.active_connections[room] = []

        # Add the user to the room
        self.active_connections[room].append(websocket)

    def disconnect(self, websocket: WebSocket, room: str):
        # Remove the user from the room
        self.active_connections[room].remove(websocket)

        # Delete the room if it's empty
        if len(self.active_connections[room]) == 0:
            del self.active_connections[room]

    async def send_personal_message(
        self,
        message: str,
        websocket: WebSocket
    ):
        await websocket.send_text(message)

    async def broadcast(self, message: str, room: str):
        # Send the message only to users in the same room
        for connection in self.active_connections[room]:
            await connection.send_text(message)