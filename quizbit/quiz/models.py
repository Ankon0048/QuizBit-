from django.db import models
from django.contrib.auth.models import User


class Questions(models.Model):
    # Primary key field for question ID
    ques_id = models.AutoField(primary_key=True)

    # Field for question number
    # This field is for listing the number of questions and showing question number
    ques_number = models.PositiveIntegerField(unique=True)

    # Field for question title
    # This field is for showing the question
    ques_title = models.CharField(max_length=255)

    # Field for question details
    # This field is for retrieving details about the question
    ques_detail = models.TextField()

    # Array field for 4 string options (MCQ having 4 options)
    # This field is for displaying the probable answers for the question
    ques_option = models.JSONField()

    # Field for the index of the correct answer
    # This field holds the index for the correct answer option
    ques_answer = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        """
        This function ensures `ques_number` is auto-incremented
        and adjusted after deletions.
        """
        if not self.pk:
            # Assign the next sequential ques_number if it's a new question
            max_number = Questions.objects.aggregate(models.Max('ques_number'))['ques_number__max'] or 0
            self.ques_number = max_number + 1

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        This function ensures to fix `ques_number` values after deletion.
        """
        super().delete(*args, **kwargs)

        # Adjust ques_number for remaining questions
        questions = Questions.objects.all().order_by('ques_number')
        for index, question in enumerate(questions, start=1):
            question.ques_number = index
            question.save()

    def __str__(self):
        return self.ques_title
