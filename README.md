# QuizBit-
A backend Restful API for an online platform based on practicing MCQ questions

## Requirements

### System Requirements
- Python 3.8 or later
- PostgreSQL database

### Python Package Dependencies
- Django
- djangorestframework
- psycopg2 (PostgreSQL adapter)

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/quizbit.git
cd quizbit
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
