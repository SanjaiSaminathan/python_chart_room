# FastAPI Chat Application - Development Notes

## Issues Faced

### 1. FastAPI import not found

**Issue**

```
Import "fastapi" could not be resolved
```

**Solution**

- Activated the virtual environment.
- Installed FastAPI using pip.
- Selected the correct Python interpreter in VS Code.

---

### 2. Uvicorn could not import app

**Issue**

```
Error loading ASGI app. Could not import module "app"
```

**Solution**

- Checked the project folder.
- Ran the server from the project root.
- Used:

```
python -m uvicorn app:app --reload
```

---

### 3. Jinja2 TemplateResponse error

**Issue**

```
TypeError: unhashable type: 'dict'
```

**Solution**

- Updated `TemplateResponse()` to:

```python
return templates.TemplateResponse(
    request=request,
    name="index.html"
)
```

---

### 4. Form data missing

**Issue**

```
Field required
username
room
```

**Solution**

- Fixed the HTML form.
- Corrected the `name` attributes:

```html
name="username" name="room"
```

---

### 5. python-multipart missing

**Issue**

```
Form data requires "python-multipart"
```

**Solution**

```bash
pip install python-multipart
```

---

### 6. WebSocket library missing

**Issue**

```
No supported WebSocket library detected
```

**Solution**

```bash
pip install "uvicorn[standard]"
```

---

### 7. Messages not appearing

**Issue**

- Messages disappeared after clicking Send.

**Solution**

- Removed duplicate `receive_text()` calls.
- Removed duplicate `broadcast()` calls.
- Corrected the JavaScript function names and element IDs.

---

### 8. Room-based WebSocket 404

**Issue**

```
GET /ws/test 404
```

**Solution**

- Updated the WebSocket URL to match the FastAPI route.

---

### 9. Username not showing

**Solution**

- Passed the username through the WebSocket URL.
- Updated the message format.

---

### 10. Added timestamps

**Solution**
Used:

```python
from datetime import datetime

timestamp = datetime.now().strftime("%H:%M:%S")
```

---

### 11. Added coloured usernames

**Solution**

- Sent JSON from FastAPI.
- Parsed JSON in JavaScript.
- Assigned a random colour to each username.

---

## Useful Commands

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment (Windows)

```bash
.\venv\Scripts\activate
```

### Install requirements

```bash
pip install -r requirements.txt
```

### Run FastAPI

```bash
python -m uvicorn app:app --reload
```

### Git

```bash
git add .
git commit -m "Commit message"
git push origin main
```
