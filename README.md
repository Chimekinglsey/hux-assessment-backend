```markdown
# Contact Manager

This project is a simple web application that allows users to manage contacts.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python installed (version 3.11 or higher)
- pip installed
- [Optional] Virtual environment set up (recommended for isolating project dependencies)

## Installation

1. Clone the repository:

**git clone https://github.com/chimekinglsey/hub-assessment-backend.git**


2. Navigate to the project directory:

```
cd hub-assessment-backend
```

3. Install the required Python dependencies:

```
pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project directory and configure the following environment variables:

```
SECRET_KEY=your_secret_key
DEBUG=True  # Set to False in production
```

## Database Setup

1. Make migrations:

```
python manage.py makemigrations
```

2. Apply migrations:

```
python manage.py migrate
```

## Running the Application

1. Start the Django development server:

```
python manage.py runserver
```

2. Access the application in your web browser at `http://localhost:8000/`

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

## Contributors

- [Chika Chime](https://github.com/chimekinglsey)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```
