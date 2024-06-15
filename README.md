# Flask Open Market Web App

Welcome to the Flask Open Market Web App! This application serves as a guide for getting started with DevOps with a Flask web framework and demonstrates a website using Flask.

## About

Flask Open Market Web App is a real website that simulates an open market, allowing different users to browse items and make purchases. Additionally, the app incorporates a budget system for each user, providing a comprehensive example of Flask application development using the Flask web framework. 

## Getting Started

To run this Flask app locally, follow these steps:

1. Clone this repository to your local machine.

``` bash
git clone https://github.com/remonagayby/devops-flask-market-app.git
```
2. Navigate to the project directory in your terminal.

3. Set up a virtual environment using

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install flask
```

4. Install the required dependencies using

```bash
pip install -r requirements.txt
```

5. Run the Flask application using

```bash
python3 run.py
```

6. Access the application in your web browser at

```bash
http://localhost:5000
```

OR through the docker hub repository

```bash
docker pull remonagayby/devops-flask-market:latest
docker run -d -p 5000:5000 remonagayby/devops-flask-market:latest
``` 


## Features

- User registration and authentication.
- Browse and purchase items from the open market.
- Budget system for managing user funds.
- Admin panel for managing items and users.

## Technologies Used

- Flask: A lightweight Python web framework.
- HTML/CSS: For designing and styling web pages.
- SQLAlchemy: Python SQL toolkit and Object-Relational Mapper.
- SQLite: Lightweight relational database management system.
- Jinja2: Templating engine for Python.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

