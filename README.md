# API FastAPI - Postgres

## 1. Getting started

This process required:
- [Python](https://github.com/pyenv/pyenv) 
- [Docker](https://github.com/pyenv/pyenv) 

To check your python version uses this command:
```bash
$ python --version
Python 3.9.13
```

## 2. Clone

Clone this repository in your local system:
```bash
git clone https://github.com/omarftt/API-FastAPI-Postgres.git
```

## 3. Installation

Create a virtual environment
```bash
virtualenv venv
source venv/bin/activate 
```

Install all packages required
```bash
cd app
pip install -r requirements.txt
```

## 4. Run the API server using docker-compose
Then, to run the development server using docker-compose, use:

```bash
cd ..
docker-compose up
```
Docker compose will up 3 services: FastAPI, Postgres, and PGAdmin. Use user and password configure in docker-compose.yml file
