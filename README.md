# Pushups-logger

## The Pushups Logger is a simple web application built to help users log their pushups with additional comments. This project implements basic user authentication, CRUD operations (Create, Read, Update, Delete), flash messages, and pagination to enhance the user experience. The front-end is built using HTML, while the back-end is powered by Python's Flask framework with SQLite as the database.

# Features
- User Authentication: Secure user sign-up and login functionality. - CRUD Operations: Users can create, view, update, and delete their pushup entries.
- Comment Section: Each pushup log entry can include optional comments.
- Flash Messages: Provides real-time feedback to users for actions like login, sign-up, and CRUD operations.
- Pagination: Displays logs across multiple pages, improving readability for large datasets.
- Responsive Frontend: Simple and clean UI built using HTML for easy user interaction.

## Technology Stack
-  Frontend: HTML, CSS
-  Backend: Python, Flask
-  Database: SQLite (SQLAlchemy ORM)
-  Other Tools: Flask-WTF (Form handling), Flask-Login (User authentication), Flask-Migrate (Database migrations), Flask-Paginate (Pagination)

## Installation

### Prerequisites
-  Python 3.x
-  pip (Python package installer)
-  SQLite (Comes bundled with Python)

### Clone the repository:
-  git clone https://github.com/srknampalli/pushups-logger.git
-  cd pushups-logger
### Create and activate a virtual environment:
-  python -m venv pushenv
-  pushhvenv\Scripts\activate

### Set up the database
-  python run db_create.py
### Run the application:
-  flask run
-  The application will be available at http://127.0.0.1:5000/.

