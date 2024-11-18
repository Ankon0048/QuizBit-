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
        fields = ['ques_id', 'ques_number', 'ques_title', 'ques_detail', 'ques_option', 'ques_answer', 'ques_difficulty', 'ques_category']


# Converts model instances into JSON format and validates input for Questions-related operations.
class HistorySerializer(serializers.ModelSerializer):
    # Include fields from the related Questions model
    ques_title = serializers.CharField(source="ques_id.ques_title", read_only=True)
    ques_number = serializers.IntegerField(source="ques_id.ques_number", read_only=True)
    ques_difficulty = serializers.CharField(source="ques_id.ques_difficulty", read_only=True)
    ques_category = serializers.CharField(source="ques_id.ques_category", read_only=True)
    ques_answer = serializers.IntegerField(source="ques_id.ques_answer", read_only=True)

    class Meta:
        model = History
        fields = ['user_id','ques_id','ques_number','ques_title', 'ques_difficulty','ques_category','ques_answer', 'user_answer', 'is_correct']
