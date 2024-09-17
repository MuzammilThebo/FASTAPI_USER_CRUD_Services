# FastAPI CRUD Service

This is a simple CRUD service built using FastAPI. The service allows you to manage user records with fields such as `username`, `password`, and `active`. It also includes JWT-based authentication and secure password storage with bcrypt.

## Features

- **Create a User**: Register a new user with a hashed password.
- **Retrieve a User**: Get user information by username.
- **Update a User**: Update the password of an existing user.
- **Deactivate a User**: Soft-delete (deactivate) a user.
- **JWT Authentication**: Implemented for secure access to protected routes.
- **Clean Code Architecture**: Follows clean code architecture for better maintainability and scalability.
- **Best Practices**: The project adheres to best practices for structuring and organizing code.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MuzammilThebo/FASTAPI_USER_CRUD_Services.git

2. Navigate into the project directory: 
    ```bash
   cd your_repository_name

3. Create a virtual environment and activate it:
    ```bash
   python -m venv venv
   source venv/bin/activate    # On Windows: venv\Scripts\activate
   
4. Install the required dependencies:
    ```bash
   pip install -r requirements.txt

5. Update the `core/config.py` file with your MySQL connection details:: 
    ```bash
   class Settings:
    SECRET_KEY = "your_secret_key_here"
    DATABASE_URL = "mysql+pymysql://<username>:<password>@localhost/<database_name>"

6. Run the application:
    ```bash
   uvicorn app.main:app --reload

7. Run the application:
    ```bash
   http://127.0.0.1:8000/docs
