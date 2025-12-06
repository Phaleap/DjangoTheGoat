# Furniture CRM Project

This is a Django-based CRM (Customer Relationship Management) system for managing furniture-related business operations. The project includes user account management, product catalog, shopping cart, checkout, and more.

## Features

- User authentication and account management
- Product catalog and detail pages
- Shopping cart and checkout process
- Blog and team pages
- Contact and about pages
- Admin interface for managing data

## Project Structure

- `accounts/` - User account management (models, views, templates)
- `crm/` - Main Django project configuration
- `static/` - Static files (CSS, JS, images, fonts)
- `templates/` - HTML templates for accounts and furniture sections
- `db.sqlite3` - SQLite database
- `manage.py` - Django management script

## Setup Instructions

1. **Clone the repository**
2. **Create and activate a virtual environment**
	- **Windows PowerShell:**
	  ```powershell
	  python -m venv env
	  .\env\Scripts\Activate.ps1
	  ```
	- **Mac/Linux (Bash):**
	  ```bash
	  python3 -m venv env
	  source env/bin/activate
	  ```
3. **Install dependencies**
	```bash
	pip install -r requirement.txt
	```
4. **Apply migrations**
	```bash
	python manage.py migrate
	```
5. **Run the development server**
	```bash
	python manage.py runserver
	```

## Requirements

The project uses the following Python packages (see `requirement.txt`):

- Django==6.0
- asgiref==3.11.0
- sqlparse==0.5.4
- tzdata==2025.2

## Usage

Access the application at `http://127.0.0.1:8000/` after starting the server. Use the admin interface at `/admin` for backend management.

## License

This project is for educational and internal business use. Please contact the author for commercial licensing.
