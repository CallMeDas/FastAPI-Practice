# FastAPI Product Management API

A simple RESTful API built with FastAPI for managing products using SQLAlchemy ORM and PostgreSQL database.

## Features

- **CRUD Operations** - Create, Read, Update, and Delete products
- **Fast & Modern** - Built with FastAPI for high performance
- **Database ORM** - SQLAlchemy for database interactions
- **PostgreSQL** - Persistent data storage with PostgreSQL
- **API Documentation** - Automatic interactive docs with Swagger UI

## Project Structure

```
FastAPI/
├── main.py                 # Main FastAPI application
├── requirements.txt        # Project dependencies
├── core/
│   └── crud.py            # CRUD operations for products
├── database/
│   ├── database.py        # Database configuration
│   ├── database_models.py # SQLAlchemy models
│   └── schemas.py         # Pydantic schemas
└── routes/
    ├── __init__.py
    └── product.py         # Product API routes
```

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd FastAPI
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Update database connection string in `database/database.py` to match your PostgreSQL setup.

## Running the Application

Start the development server:

```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

- **Swagger UI** (Interactive): `http://localhost:8000/docs`
- **ReDoc** (Alternative docs): `http://localhost:8000/redoc`

## API Endpoints

### Base URL
`http://localhost:8000`

### Product Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Health check |
| GET | `/products/` | Get all products |
| GET | `/products/{product_id}` | Get product by ID |
| POST | `/products/` | Create a new product |
| PUT | `/products/{product_id}` | Update a product |
| DELETE | `/products/{product_id}` | Delete a product |



## Dependencies

- **fastapi** - Web framework
- **uvicorn** - ASGI server
- **sqlalchemy** - ORM
- **psycopg2** - PostgreSQL adapter

See `requirements.txt` for all dependencies.

## Database Setup

Ensure PostgreSQL is installed and running. The application will automatically create tables based on the SQLAlchemy models when started.

## Development

The application uses automatic database table creation via SQLAlchemy. Models are defined in `database/database_models.py`.


