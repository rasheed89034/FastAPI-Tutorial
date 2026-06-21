# FastAPI-Tutorial

# 🚀 FastAPI: The Modern Web Framework (A to Z)

**FastAPI** is a modern, extremely fast (high-performance), and easy-to-learn web framework for building RESTful APIs with Python 3.8+. It is fundamentally based on standard Python type hints.

## 🧠 Under the Hood (How it Works)
FastAPI does not reinvent the wheel. It stands on the shoulders of two major, highly-optimized Python libraries:
1. **Starlette:** Handles the web parts (routing, HTTP requests, WebSockets, and asynchronous processing).
2. **Pydantic:** Handles the data parts (data validation, serialization, and JSON schema generation).

## 🌟 Key Features & Details

### 1. ⚡ Extreme Performance
FastAPI is one of the fastest Python frameworks available, rivaling NodeJS and Go. It runs on an **ASGI** (Asynchronous Server Gateway Interface) server like **Uvicorn**, making it perfectly suited for handling concurrent requests and long-running background tasks without blocking the main thread.

### 2. 🛡️ Automatic Data Validation
You do not need to write complex logic to check if a user sent an integer, a valid email, or a string. FastAPI uses Python Type Hints and **Pydantic**. If a client sends invalid data (e.g., passing text where a number is expected), FastAPI automatically rejects the request and returns a clear, structured JSON error indicating exactly which field was wrong.

### 3. 📖 Auto-Generated Interactive Documentation
You never have to write API documentation manually. FastAPI automatically generates dynamic, interactive API documentation based on the **OpenAPI** standard:
* **Swagger UI** (`/docs`): Allows you to test and call your API endpoints directly from the browser.
* **ReDoc** (`/redoc`): Provides a clean, highly readable, deep-dive documentation format.

### 4. 💉 Dependency Injection System
FastAPI includes an incredibly powerful but easy-to-use Dependency Injection system. This allows you to effortlessly share logic across multiple endpoints (such as checking user authentication, opening database sessions, or validating tokens) without writing repetitive code.

### 5. 🔒 Built-in Security and Authentication
FastAPI integrates seamlessly with industry-standard security protocols. It provides built-in tools to handle:
* **OAuth2** (with JWT Tokens)
* **Password Hashing** (via Passlib)
* API Keys and HTTP Basic Auth

### 6. 🌐 Native Asynchronous Support
FastAPI was built with `async` and `await` at its core. It natively supports asynchronous database connections, making it highly efficient for I/O-bound operations (like fetching data, calling other APIs, or sending emails).

### 7. Editor Support & Developer Experience
Because everything is based on Python type hints, editors like VS Code and PyCharm provide excellent autocompletion and type-checking everywhere. This speeds up development by 200% to 300% and drastically reduces bugs.

---

## 🚀 Quick Start Example

Here is how simple it is to create a fully-fledged, validated endpoint in FastAPI:

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    cgpa: float

@app.post("/students/")
def create_student(student: Student):
    # FastAPI automatically validates that 'age' is an int and 'cgpa' is a float!
    return {"message": "Student created successfully", "data": student}
