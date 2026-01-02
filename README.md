
<h1>🚀  FastAPI + PostgreSQL Project</h1>
A backend application built using <b>FastAPI</b> with <b>PostgreSQL</b> as the database.<br>
This project demonstrates clean API design, database integration, and best practices for building scalable backend services.<br>

---

<h3>📌  Features</h3>

- High performance REST APIs using FastAPI
- PostgreSQL Integration
- Modular project structure
- Pydantic models for request/response validation
- Environment-based configuration
- Easy to extend for authentication, pagination, and async operations

---

<h3>🏗️  Tech Stack</h3>

- <b>Backend Framework</b>: FastAPI
- <b>Language</b>: Python 3.12+
- <b>Database</b>: Postgre SQL
- <b>ORM</b>: SQLAlchemy
- <b>Validation</b>: Pydantic
- <b>Server</b>: uvicorn

---

<h3> 📂 Project Structure </h3>

``` text
fastapi_postgre/
│
├── app/
│   ├── main.py            # FastAPI entry point
│   ├── models.py          # Database models
│   ├── schemas.py         # Pydantic schemas
│   ├── database.py        # DB connection
│   └── curd.py            # DB operations
│
├── requirements.txt
├── README.md
└── .env
```

---

 <h3>⚙️ Prerequisties</h3>

 Make sure you have :
 - Python 3.12 or higher
 - PostgreSQL installed and running
 - uv or pip
  
---

<h3> 🛠️ Setup & Installation </h3>

<h4> 1️⃣ Clone the repository </h4>

```
git clone https://github.com/Satyanarayana06b/fastapi_postgre.git
cd fastapi_postgre
```

<h4> 2️⃣ Create virtual environment </h4>

```
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

<h4> 3️⃣ Install dependencies </h4>

```
pip install -r requirements.txt
```

---


<h3> 🔐 Environment Configuration </h4>
Create a `.env` file in the root directory.

```
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
```

---


<h3> ▶️ Run the Application </h4>

```
uvicorn app.main:app --reload
```

Application will be available at 

```
http://127.0.0.1:8000
```

---

<h3> 📘 API Documentation (Swagger) </h3>

FastAPI provides built-in inteactive documentation:

- Swagger UI: 
  ```
  http://127.0.0.1:8000/docs
  ```

- ReDoc: 
  ```
  http://127.0.0.1:8000/redoc
  ```

---

<h3> 🧪 API Endpoints </h3>

| Method | Endpoint | Description |
|------|---------|-------------|
| GET | `/health` | Health Check |
| GET | `/items` | Fetch Items |
| GET | `/items/{item_id}` | Fetch item using id |
| POST | `/items` | Create an item |
| PUT | `/items/{item_id}` | Update item using id |
| DELETE | `/items/{item_id}` | Delete item using id |

---

<h3>🚧 Future Enhancements</h3>

- JWT Authentication & Authorization
- Async database support
- Pagination & filtering
- Docker
- Unit & Integration testing
- CI/CD Pipeline
- Architecture Diagram

---

<h3> 👨‍💻 Author </h3>

<b>Satyanarayana (Satya)</b>

🔗 GitHub: https://github.com/Satyanarayana06b

---
