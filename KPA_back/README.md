# KPA Backend Assignment – API Implementation

## Overview

This project is a backend implementation of two APIs selected from the provided Postman collection. The APIs are built using **FastAPI** and **PostgreSQL**, with adherence to the structure and specifications outlined in the Swagger documentation.

---

## Tech Stack

- **Backend Framework:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Testing Tool:** Postman
- **API Docs:** Swagger UI (`/docs`)

---

## Key Features Implemented

1. **POST `/api/forms/wheel-specifications`**  
   → Creates a new Wheel Specification record in the database.  
   → Validates incoming payload and returns `201 Created`.

2. **GET `/api/forms/wheel-specifications`**  
   → Retrieves filtered list of Wheel Specification records.  
   → Supports query-based filtering and returns `200 OK`.

---

## How to Set Up the Project

### 1. Clone the repository

```bash
git clone https://github.com/nidhimahagaonkar-03/kpa-backend.git
cd kpa-backend
```

### 2. Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up PostgreSQL and the `.env` file

Create a PostgreSQL database (e.g., `kpa_db`) and a `.env` file in the project root with:

```env
DATABASE_URL=postgresql://your_username:your_password@localhost:5432/kpa_db
```

Make sure this matches the connection format used in `database.py`:

```python
from dotenv import load_dotenv
import os

load_dotenv()
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL")
```

Install `python-dotenv` if not already:

```bash
pip install python-dotenv
```

### 5. Run the server

```bash
uvicorn app.main:app --reload
```

> The server will be available at `http://127.0.0.1:8000`

### 6. API Documentation

Visit Swagger UI at:  
`http://127.0.0.1:8000/docs`

---

## Testing the API with Postman

1. Import the original or updated Postman collection.
2. Change request URLs to:
   ```
   http://localhost:8000/api/forms/wheel-specifications
   ```
3. Test with:
   - Valid data → Expect `201 Created` or `200 OK`
   - Invalid data → Expect proper validation errors (`400`, `422`)

---

## Assumptions & Limitations

- Basic validation is handled by FastAPI's Pydantic models.
- No user authentication or authorization implemented.
- Only two endpoints are implemented as per the assignment.
- Error handling is minimal — could be expanded in future versions.
- Filtering logic is basic and can be extended (e.g., pagination, sorting).

---

## 📎 Files Included

- `main.py` – FastAPI app entry point
- `models.py` – SQLAlchemy DB models
- `schemas.py` – Pydantic request/response models
- `database.py` – DB connection
- `.env` – Environment configuration (ignored by Git)
- `app/` – Contains API logic and structure
- `KPA_Updated_Collection.postman_collection.json` – Postman collection

---

## ✅ Final Note

This submission fulfills all the assignment requirements, including:
- Endpoint structure
- Functional implementation
- Database operations
- Documentation & Postman testing

---