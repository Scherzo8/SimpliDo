# SimpliDo
A simple and efficient Todo application built with FastAPI and PostgreSQL. This application allows users to create, read, update, and delete tasks while managing user authentication.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#Technologies-Used)
- [Requirements](#requirements)
- [Installation Instruction](#Installation-Instruction)
- [License](#license)

## Overview

This Application is a robust and user-friendly task management tool designed to streamline your productivity. Built on the FastAPI framework, this application leverages the power of Python and PostgreSQL to provide a seamless experience for managing tasks. Users can register, authenticate, and create tasks with detailed descriptions and status tracking.

This application features API endpoints that allow for efficient task management, including the ability to create, read, update, and delete tasks. With a focus on performance and scalability, the FastAPI Todo Application is an ideal solution for anyone looking to manage projects effectively.

In addition to core functionality, the application is structured for ease of development and maintenance, making it suitable for both personal use and as a foundational project for developers looking to expand their knowledge of FastAPI, SQLAlchemy, and PostgreSQL.

## Technologies Used
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/) for database interaction
- [PostgreSQL](https://www.postgresql.org/) as the database
- [Poetry](https://python-poetry.org/) for dependency management
- [Pydantic](https://pydantic-docs.helpmanual.io/) for data validation


## Features

- User registration and authentication
- Create, read, update, and delete tasks
- Store tasks with titles, descriptions, and completion status


## Requirements

- Python 3.12 or later
- PostgreSQL installed and running
- Poetry for managing dependencies


## Installation Instruction: 

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Scherzo8/SimpliDo.git
   cd SimpliDo
   ```
2. **Install dependencies:**
    ```bash
    poetry install
    ```

3. **Configure environment variables:**  

    Create a `.env` file in the project root and add your database URL and Secret key:  

    `DATABASE_URL=postgresql://username:password@localhost/todo_app`  

    `SECRET_KEY="add-your-secret-key"`


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---
