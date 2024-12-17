# Flask Web Application with Docker and Persistent Storage
## Project Description
This project is a simple web application built with Flask. It includes:

1. Two HTML pages with routing: index.html and message.html.
2. Form processing to save messages into a data.json file.
3. A route /read to display saved messages using a Jinja2 template.
3. Custom 404 error page (error.html).
4. Application containerized with Docker, using volumes for persistent storage of data.json outside the container.

## Installation and Setup
1. Clone the Repository

git clone https://github.com/your-username/goit-pythonweb-hw-03.git
cd goit-pythonweb-hw-03

2. Create a Virtual Environment (Optional)

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Run the Application Locally

python app.py

Visit http://127.0.0.1:3000.

## Docker Setup
1. Build and Run with Docker Compose
Ensure Docker Desktop is running, then execute:

docker-compose up --build

2. Access the Application
* Home Page: http://localhost:3000
* Message Page: http://localhost:3000/message
* Read Messages: http://localhost:3000/read
* 404 Error Page: Visit any invalid route, e.g., http://localhost:3000/invalid.