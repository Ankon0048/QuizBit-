from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re


class Questions(models.Model):
    # Primary key field for question ID
    ques_id = models.AutoField(primary_key=True)

    # Field for question number
    # This field is for showing question number
    ques_number = models.PositiveIntegerField(unique=True)

    # Field for question title
    # This field is for showing the question
    ques_title = models.TextField()

    # Field for question details
    # This field is for showing additional information about the question
    ques_detail = models.TextField()

    # Array field for 4 string options (MCQ having 4 options)
    # This field is for displaying the probable answers for the question
    ques_option = models.JSONField()

    # Field for the index of the correct answer
    # This field holds the index for the correct answer option
    ques_answer = models.PositiveIntegerField()


    # Field for question difficulty
    # This can take only three values: Easy, Medium, Hard (For now it's statically defined)
    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Medium', 'Medium'),
        ('Hard', 'Hard'),
    ]
    ques_difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='Medium',
    )

    # Field for question category
    # This can take a predefined range of string values (For now it's statically defined)
    CATEGORY_CHOICES = [
        ('Math', 'Math'),
        ('Science', 'Science'),
        ('History', 'History'),
        ('Geography', 'Geography'),
        ('Technology', 'Technology'),
    ]
    ques_category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Math',
    )

    def save(self, *args, **kwargs):
        """
        This function ensures ques_number is auto-incremented
        and adjusted after deletions.
        """
        if not self.pk:
            # Assign the next sequential ques_number if it's a new question
            max_number = Questions.objects.aggregate(models.Max('ques_number'))['ques_number__max'] or 0
            self.ques_number = max_number + 1

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):

        # This function ensures to fix ques_number values after deletion.

        super().delete(*args, **kwargs)

        # Adjust ques_number for remaining questions
        questions = Questions.objects.all().order_by('ques_number')
        for index, question in enumerate(questions, start=1):
            question.ques_number = index
            question.save()

    def __str__(self):
        return self.ques_title



class Users(models.Model):
    # Primary key field for users
    user_id = models.AutoField(primary_key=True)

    # Username with restricted special characters
    # Username is restricted to 15 characters and allows only letters, numbers, underscores and dots.
    # Uses regex for checking validity.
    user_name = models.CharField(
        max_length=15,
        unique=True,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z0-9_.]+$',
                message="Username can only contain letters, numbers, underscores, and dots.",
            )
        ]
    )

    # Encrypted password
    # Password is hashed before saving in the database
    password = models.CharField(
        max_length=128  # Default max length for Django password hashes
    )

    # Email validation
    email = models.EmailField(unique=True)

    def save(self, *args, **kwargs):
        if not re.search(r'\s', self.password):  # Ensure no spaces in the password
            self.password = make_password(self.password)
        else:
            raise ValueError("Password cannot contain spaces.")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user_name


class History(models.Model):
    # Foreign key referencing the Users table
    user_id = models.ForeignKey('Users', on_delete=models.CASCADE)

    # Foreign key referencing the Questions table
    ques_id = models.ForeignKey('Questions', on_delete=models.CASCADE)

    # Answer provided by the user
    answer = models.PositiveIntegerField()

    # Boolean field for correctness
    is_correct = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        """
        Method to determine if the answer is correct
        based on the ques_answer field in the Questions table.
        """
        if not self.ques_id:
            raise ValidationError("Question ID cannot be null.")

        # Check if the user's answer matches the correct answer
        correct_answer = self.ques_id.ques_answer  # Get correct answer from the related question
        self.is_correct = (self.answer == correct_answer)

        super().save(*args, **kwargs)

    def __str__(self):
        return f"User: {self.user_id.user_name}, Question: {self.ques_id.ques_title}, Correct: {self.is_correct}"