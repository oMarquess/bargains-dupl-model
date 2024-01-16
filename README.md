# Django Rest Framework Project: Product Existence Checker

## Overview
This Django project leverages the Django Rest Framework to provide an API that accepts a product name as input and returns `True` if it exists in the database, or `False` if it doesn't.

## Requirements
- Python 3.x
- Django
- Django Rest Framework
- Other dependencies listed in `requirements.txt`

## Setup

### Installing Dependencies
Install the necessary packages with the following command:

```bash
pip install -r requirements.txt
```

### Setting Up the Database
This project uses a Chroma database. Ensure it is set up and configured in your Django settings.

### Running Migrations
Apply migrations using this command:

```bash
python manage.py migrate
```

## Usage

### Starting the Server
Start the Django server with:

```bash
python manage.py runserver
```

### Checking Product Existence
To check if a product exists, send a GET request to `/api/query/<product_name>`.

Example:

```bash
curl http://localhost:8000/api/query/product_name
```

### Adding Products to Database
Add products to the database using the custom `file_handler` command with your data file's path:

```bash
python manage.py file_handler <file_path>
```

## Custom Management Command: file_handler

### Purpose
This command is designed to process a file with product names, split and embed the data, and then store it in the Chroma database.

### Usage
Execute the command with the following syntax, replacing `<file_path>` with your data file's path:

```bash
python manage.py file_handler file_path
```

## Contributing
Guidelines for contributing to this project.

## License
Apache 2.0
```
