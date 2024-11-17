from rest_framework import serializers
from .models import Users, Questions, History


# Converts model instances into JSON format and validates input for Users-related operations.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['user_id', 'user_name', 'email']


# Converts model instances into JSON format and validates input for Questions-related operations.
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ['ques_id', 'ques_number', 'ques_title', 'ques_detail', 'ques_option', 'ques_answer']


# Converts model instances into JSON format and validates input for Questions-related operations.
class HistorySerializer(serializers.ModelSerializer):

    # Used PrimaryKeyRelatedField to represent relationships (ForeignKey) to other models
    user_id = serializers.PrimaryKeyRelatedField(queryset=Users.objects.all())
    ques_id = serializers.PrimaryKeyRelatedField(queryset=Questions.objects.all())

    class Meta:
        model = History
        fields = ['user_id', 'ques_id', 'answer', 'is_correct']
        read_only_fields = ['is_correct']
