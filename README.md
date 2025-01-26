# Django-Quiz-App

## Project Setup Instructions

### Prerequisites

- Python 3.12 or higher
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/your-username/django-quiz-app.git
    cd django-quiz-app
    ```

2. Create and activate a virtual environment:

    ```sh
    python -m venv .venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install dependencies:

    ```sh
    poetry install
    ```

4. Set up environment variables:

    Copy the  file to  and adjust the settings as needed.

    ```sh
    cp .env.example .env
    ```

5. Apply database migrations:

    ```sh
    cd src
    python manage.py migrate
    ```

6. Run the development server:

    ```sh
    python manage.py runserver
    ```

6. Alternatively, use Makefile to run migrations and start development server:

    ```sh
    make server
    ```



### Usage

- Access the application at http://127.0.0.1:8000/
- Admin interface at http://127.0.0.1:8000/admin

### Running Tests

To run tests, use the following command:

```sh
python manage.py test
```