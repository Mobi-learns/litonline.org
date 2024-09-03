LIT Scholarship Application
Overview

The LIT Scholarship Application is a web-based platform designed to manage and present scholarship information efficiently. This application is built using Flask for the backend and utilizes Apache for web hosting. The system is containerized using Docker and can be deployed on various environments.
Features

    Home Page: Displays an overview and welcome message.
    About Page: Information about the scholarship program.
    Apply Page: Allows users to submit applications.
    Contact Page: Provides a form for users to get in touch.
    Scholarships Page: Lists available scholarships with detailed descriptions.

Project Structure

The project directory is organized as follows:

php
Copy code
/var/www/html/
├── __pycache__               # Compiled Python files
├── index.html                # Static HTML file for the homepage
└── litonline
    ├── myapp
    │   ├── __pycache__       # Compiled Python files
    │   ├── app.py            # Main Flask application file
    │   ├── app1.py           # Additional Python script
    │   ├── config.py         # Configuration file
    │   ├── myapp.wsgi        # WSGI entry point for the application
    │   ├── static
    │   │   └── css
    │   │       └── styles.css # CSS styles for the application
    │   └── templates
    │       ├── about.html    # HTML template for the About page
    │       ├── apply.html    # HTML template for the Apply page
    │       ├── contact.html  # HTML template for the Contact page
    │       ├── index.html    # HTML template for the Home page
    │       └── scholarships.html # HTML template for the Scholarships page
    └── requirements.txt       # List of Python dependencies

Installation
Prerequisites

    Python 3.10
    Apache2
    Docker and Docker Compose (for containerization)

Setup

    Clone the Repository:

    bash
    Copy code
    git clone https://github.com/Mobi-learns/litonline.org.git
    cd litonline.org

    Install Dependencies:

    Make sure you have the required Python packages:

    bash
    Copy code
    pip install -r requirements.txt

    Configure Apache:

    Ensure the Apache configuration is set up to use WSGI and SSL. Update your /etc/apache2/sites-available/litonline.conf and /etc/apache2/sites-available/litonline-le-ssl.conf files accordingly.

    Set Up Docker (Optional):

    Build and run the Docker container:

    bash
    Copy code
    sudo docker build -t litonline-app .
    sudo docker run -d -p 80:80 litonline-app

    Configure SSL (Optional):

    Follow the steps to obtain and configure an SSL certificate using Certbot:

    bash
    Copy code
    sudo certbot --apache -d www.litonline.org

Usage

    Run the Flask Application:

    If not using Docker, start the Flask application using WSGI:

    bash
    Copy code
    sudo service apache2 restart

    Access the Application:

    Open your web browser and navigate to http://www.litonline.org or https://www.litonline.org if SSL is configured.

Contributing

We welcome contributions to improve the LIT Scholarship Application. Please follow these guidelines:

    Fork the Repository:
    Create a Feature Branch:
    Commit Your Changes:
    Push to the Branch:
    Open a Pull Request:

For detailed instructions, please refer to our CONTRIBUTING.md file.
License

This project is licensed under the MIT License - see the LICENSE file for details.
Contact

For any queries or support, please reach out to:

    Project Maintainer: Your Name
    GitHub Repository: https://github.com/Mobi-learns/litonline.org
