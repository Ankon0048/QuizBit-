# QuizBit-
A backend Restful API for an online platform based on practicing MCQ questions

## Requirements

### System Requirements
- Python 3.8 or later
- Postgresql (Optional)
- Postman

### Python Package Dependencies
- Django
- djangorestframework
- psycopg2 (PostgreSQL adapter)

## Installation Guide

### 1. Clone the repository
```bash
git clone https://github.com/your-username/quizbit.git
```
### 2. Install the required libraries
Open a command line terminal in the cloned repository folder
```bash
pip install -r requirements.txt
```

### 3. Go to the quizbit folder
```bash
cd quizbit
```
### 4. Run the below command to start the project
```bash
python manage.py runserver
```

## Testing Guide

### 1. Use this api link to access the collection for the Quizbit API in Postman
```bash
https://api.postman.com/collections/39736566-cddd08ea-1a9c-4313-9c14-b11aac98b02f?access_key=PMAT-01JCZJ3H1WXE7FSNT344TRV4B7
```
### 2. Manual instructions for testing

####  To retrieve a list of questions [GET]
```bash
http://127.0.0.1:8000/questions
```
####  To get question details [GET]
http://127.0.0.1:8000/questions/<ques_id>
```bash
http://127.0.0.1:8000/questions/3
```
####  To submit answer to a question [POST]
```bash
http://127.0.0.1:8000/submit-answer/
```
For the body of this request
enter valid data in the fields
```bash
{
  "user_id": 3,
  "ques_id": 3,
  "user_answer": 3
}
```
#### To retrieve a user's practice history [GET]
http://127.0.0.1:8000/user-history/<user_id>
```bash
http://127.0.0.1:8000/user-history/3/
```

## System Design Documentation

### 1. Core Components

- **Framework**: Django (Python)
- **Database**: PostgreSQL
- **API**: RESTful APIs using Django REST Framework (DRF)

### 2. Key Features
1. Handles requests via REST APIs and provides response in JSON format
2. Manages data validation and relationship between different models.
3. Ensures auto-incrementing question numbers and validation of user-provided answers.
4. User password is securely stored in the database in encrypted form.

### 3. Database Schema

### **Users Table**
| Field      | Type       | Description                                                              |
|------------|------------|--------------------------------------------------------------------------|
| `user_id`  | AutoField  | Primary Key for the user.                                                |
| `user_name`| CharField  | Unique username with restrictions on allowed characters.                 |
| `password` | CharField  | Encrypted password stored securely.                                      |
| `email`    | EmailField | Unique email address for the user.                                       |

---

### **Questions Table**
| Field            | Type           | Description                                                              |
|-------------------|----------------|--------------------------------------------------------------------------|
| `ques_id`        | AutoField      | Primary Key for the question.                                            |
| `ques_number`    | PositiveInt    | Auto-incremented question number.                                        |
| `ques_title`     | TextField      | Title or text of the question.                                           |
| `ques_detail`    | TextField      | Additional Information about the question                                |
| `ques_option`    | JSONField      | List of multiple-choice options for the question.                        |
| `ques_answer`    | PositiveInt    | Index of the correct answer. (0-based indexing)                          |
| `ques_difficulty`| CharField      | Difficulty of the question: Easy, Medium, Hard.                          |
| `ques_category`  | CharField      | Category of the question (Static): e.g., Math, Science, History, etc.    |

---

### **History Table**
| Field       | Type         | Description                                      |
|-------------|--------------|--------------------------------------------------|
| `user_id`   | ForeignKey   | References Users.                                |
| `ques_id`   | ForeignKey   | References Questions.                            |
| `user_answer`| PositiveInt  | User's submitted answer.                    |
| `is_correct`| BooleanField | True if the user's answer matches the correct answer. |

---
