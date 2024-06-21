# Adventrack API

This is a Flask-based API for user authentication, destination management, and travel recommendations.

## Setup

1. Install dependencies:
    ```sh
    pip install -r requirements.txt
    ```

2. Set up your `.env` file with the necessary environment variables:
    ```plaintext
    FLASK_APP=app.py
    FLASK_ENV=development
    DB_USER=your_db_user
    DB_PASS=your_db_password
    DB_NAME=your_db_name
    DB_SOCKET=/cloudsql/your_project_id:region:instance_id
    SQLALCHEMY_DATABASE_URI=mysql+pymysql://your_db_user:your_db_password@/your_db_name?unix_socket=/cloudsql/your_project_id:region:instance_id
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    PORT=8080
    ```

3. Initialize the database:
    ```sh
    flask db init
    flask db migrate
    flask db upgrade
    ```

4. Run the application:
    ```sh
    flask run
    ```

## Endpoints

### Authentication

- **Register**
    - `POST /register`
    - Request Body: `{ "username": "string", "email": "string", "password": "string" }`
    - Response: `{ "message": "User registered successfully" }`

- **Login**
    - `POST /login`
    - Request Body: `{ "email": "string", "password": "string" }`
    - Response: `{ "message": "Login successful", "user_id": "integer" }`

### Users

- **Get All Users**
    - `GET /users`
    - Response: `[{ "id": "integer", "username": "string", "email": "string" }]`

- **Get User by ID**
    - `GET /users/<id>`
    - Response: `{ "id": "integer", "username": "string", "email": "string" }`

### Destinations

- **Get All Destinations**
    - `GET /destinations`
    - Response: `[{ "id": "integer", "place_name": "string", "description": "string", "category": "string", "city": "string", "price": "float", "rating": "float", "time_minutes": "integer", "latitude": "float", "longitude": "float", "pictures": "string" }]`

- **Get Destination by ID**
    - `GET /destinations/<id>`
    - Response: `{ "id": "integer", "place_name": "string", "description": "string", "category": "string", "city": "string", "price": "float", "rating": "float", "time_minutes": "integer", "latitude": "float", "longitude": "float", "pictures": "string" }`

- **Search Destinations by Name**
    - `GET /destinations/search/name`
    - Query Params: `name=string`
    - Response: `[{ "id": "integer", "place_name": "string", "description": "string", "category": "string", "city": "string", "price": "float", "rating": "float", "time_minutes": "integer", "latitude": "float", "longitude": "float", "pictures": "string" }]`

- **Search Destinations by City**
    - `GET /destinations/search/city`
    - Query Params: `city=string`
    - Response: `[{ "id": "integer", "place_name": "string", "description": "string", "category": "string", "city": "string", "price": "float", "rating": "float", "time_minutes": "integer", "latitude": "float", "longitude": "float", "pictures": "string" }]`

- **Create Destination**
    - `POST /destinations`
    - Request Body: `{ "place_name": "string", "description": "string", "category": "string", "city": "string", "price": "float", "rating": "float", "time_minutes": "integer", "latitude": "float", "longitude": "float", "pictures": "string" }`
    - Response: `{ "message": "Destination created successfully", "id": "integer" }`

### Recommendations

- **Get Travel Recommendations**
    - `POST /predict`
    - Request Body: `{ "destination_id": "integer" }`
    - Response: 
    ```
    [{ "id": "integer", "place_name": "string", "description": "string", "category": "string", "city": "string", "price": "float", "rating": "float", "time_minutes": "integer", "latitude": "float", "longitude": "float", "pictures": "string" }]
    ```
