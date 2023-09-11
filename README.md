# Corbado Authentication with Flask

## Project Overview

This project implements a web application with a login system using the Corbado authentication service integrated with a Flask backend. The application consists of two main pages: a login page and a home page. Once users log in successfully via the Corbado service on the login page, they are redirected to the home page where they can log out and view some content.

## Tools and Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python, used to build the backend of the application.
- **Corbado**: An authentication service used to handle user login.
- **Python-dotenv**: A Python package to read key-value pairs from a `.env` file and set them as environment variables.
- **HTML & CSS**: Used to structure and style the frontend of the application.

## Features

- **Secure Authentication**: Utilizes Corbado's authentication service for secure user login.
- **Environment Variables**: Uses environment variables to securely store and manage sensitive information like project ID.
- **Dynamic Content**: Displays dynamic content on the home page based on the user's authentication status.

## How to Use

### Step 1: Clone the Repository

Clone this repository to your local machine by running:

```sh
git clone https://github.com/chigozz/flask-corbado

```

### Step 2: Update .env File

Replace `your_project_id_here` with your project ID in the environment variable code below:

```sh
PROJECT_ID=your_project_id_here
```
### Step 3: Install Project Packages

Run the following command to install the project packages specified in the requirements.txt file:

```sh
pip install -r requirements.txt
```

### Step 4: Run the Project

Use the following command to run the project:

```sh
python corbado-auth.py
```