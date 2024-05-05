# Contact Manager

This project is a simple web application that allows users to manage contacts.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python installed (version 3.11 or higher)
- pip installed
- [Optional] Virtual environment set up (recommended for isolating project dependencies)

## Installation

1. Clone the repository:
```
git clone https://github.com/chimekinglsey/hub-assessment-backend.git
```

## Configuration

1. Create a `.env` file in the project directory and configure the following environment variables:

```
DB_NAME=your_database_name
DB_USER=your_database_user
DB_PASSWORD=your_database_password
DB_HOST=your_database_host
DB_PORT=your_database_port
SECRETS=your_secrets_key
DJANGO_SECRETS=your_django_secrets_key
```


## Running the Application

Follow these steps to run the application:

### Backend (Django)

1. Create a virtual environment (optional but recommended):

```
python3 -m venv venv
```

2. Activate the virtual environment:

```
source venv/bin/activate
```

3. Install the required Python packages:

```
pip install -r requirements.txt
```

4. Configure your database:
   - Create a MySQL database named `contact_manager`.
   - Ensure that the user has permissions to administer the database.

5. Apply migrations to the database:

```
python manage.py makemigrations
python manage.py migrate
```

6. Start the Django development server:

```
python manage.py runserver
```

7. Access the application in your web browser at `http://localhost:8000/`

### Frontend (React)

1. Navigate to the frontend directory:

```
cd hux-assessment-frontend
```

2. Install dependencies:

```
npm install
```

3. Start the React development server:

```
npm run dev
```

4. Access the application in your web browser at the provided URL (typically `http://localhost:5173/`)

## API Endpoints

- **/auth/register/** - User registration endpoint.
- **/auth/login/** - User login endpoint.
- **/api/token/** - Obtain JWT token pair.
- **/api/token/refresh/** - Refresh JWT token.
- **/contacts/** - List and search contacts (GET).
- **/contacts/<int:pk>/** - Retrieve contact details (GET), Update contact details (PUT), Delete contact (DELETE).
- **/contacts/** - Create new contact (POST).

## Testing

To run tests, execute the following command:

```
python manage.py test
```

Please ensure that you have MySQL installed and configured correctly before running the application. If you encounter any issues or have any questions, feel free to reach out for assistance.## Contributors

- [Chika Chime](https://github.com/chimekinglsey)


