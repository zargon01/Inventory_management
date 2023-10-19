# Inventory Management System

An inventory management system built with Flask and MySQL for tracking products, their descriptions, and quantities.

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Add, edit, and delete products.
- View a list of products with their details.
- Aesthetic and responsive web interface.
- MySQL database for data storage.
- Simple API for managing inventory data.

## Project Structure

The project is structured as follows:

inventory_management/
│
├── app.py # Flask application
├── templates/ # HTML templates
│ ├── base.html
│ ├── index.html
│ ├── add_product.html
│ ├── edit_product.html
├── static/ # Static files (CSS, favicon)
│ ├── style.css
│ ├── favicon.ico
│
├── models.py # SQLAlchemy models
├── config.py # Configuration settings


## Dependencies

This project relies on the following dependencies:

- Python 3.9+
- Flask: Web framework for Python
- Flask-SQLAlchemy: SQLAlchemy extension for Flask
- MySQL database (you can replace this with your preferred database)
- Other packages mentioned in [requirements.txt](requirements.txt)

You can install these dependencies using the following command:

```bash
pip install -r requirements.txt
```

## Installation

  1. Clone the repository to your local machine:
  2. ```bash
       git clone https://github.com/yourusername/inventory-management.git
       cd inventory-management
     ```
  3. Set up a virtual environment (optional but recommended):
     ```bash
       python -m venv venv
     ```
  5. Install the project dependencies:
  6. ```bash
      pip install -r requirements.txt
     ```
  7. Create a MySQL database and update the SQLALCHEMY_DATABASE_URI in config.py with your database connection details.
  8. Run the application:
  9. ```bash
     python app.py
     ```
The application should be accessible at http://localhost:5000.



## Usage
 - Access the web application in your browser and start managing your inventory.
 - Use the API endpoints for programmatic access to the inventory data.

