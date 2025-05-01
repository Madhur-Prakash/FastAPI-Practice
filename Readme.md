# FastAPI Practice

A practice repository for building and experimenting with FastAPI — a modern, fast (high-performance), web framework for building APIs with Python 3.10+ based on standard Python type hints.

## 🚀 Features

- FastAPI fundamentals and routing
- Request handling with Pydantic models
- Path and query parameters
- Basic middleware usage
- Modular code structure
- JSON response handling
- Environment variable usage
- Local development setup with `uvicorn`

---

## Technology Stack
- **Backend Framework**: FastAPI
- **Database**: SQLAlchemy  
- **Password Hashing**: [bcrypt or any other hashing library used]
- **Programming Language**: Python

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Madhur-Prakash/FastAPI-Practice.git
   ```
2. Navigate to the project directory:
   ```bash
   cd FastAPI-Practice
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Set up SQLAlchemy -> Run the following commands in the terminal:
  ```bash
python
from app import app,db 
with app.app_context():
    db.create_all() 
exit()
```
---

## 📁 Project Structure
```plaintext
FastAPI-Practice/
├── .gitignore  # gitignore file for GitHub
├── app.py  # main FastAPI app
├── blog
│   ├── __init__.py  # initializes package
│   ├── database.py
│   ├── hashing.py
│   ├── main.py
│   ├── models.py  # models
│   ├── oauth2.py
│   ├── repository
│   │   ├── blog.py
│   │   └── user.py
│   ├── routers
│   │   ├── __init__.py  # initializes package
│   │   ├── authentication.py
│   │   ├── blog.py
│   │   └── user.py
│   ├── schemas.py
│   └── token.py
├── blog.db
└── requirements.txt
```

---
## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Author
**Madhur Prakash**  
[GitHub](https://github.com/Madhur-Prakash) | [Medium](https://medium.com/@madhurprakash2005)

---



