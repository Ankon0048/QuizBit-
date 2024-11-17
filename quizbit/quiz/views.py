from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Users, Questions, History
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
import re
from .serializers import UserSerializer, QuestionSerializer, HistorySerializer
from django.http import HttpResponse
from django.views import View


# A serializer to only get the question title and question number
class QuestionListSerializer(serializers.Serializer):
    ques_title = serializers.CharField()
    ques_number = serializers.IntegerField()


# API to retrieve all questions
class QuestionListView(APIView):
    def get(self, request):
        questions = Questions.objects.values('ques_title', 'ques_number')  # Fetch only required fields
        serializer = QuestionListSerializer(questions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to get question details
class QuestionDetailView(APIView):
    def get(self, request, ques_id):
        try:
            question = Questions.objects.get(ques_id=ques_id)
        except Questions.DoesNotExist:
            return Response({"error": "Question not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionSerializer(question)
        return Response(serializer.data, status=status.HTTP_200_OK)


# API to submit an answer
class SubmitAnswerView(APIView):
    def post(self, request):
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # save() will auto-set "is_correct" field
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# API to retrieve user history
class UserHistoryView(APIView):
    def get(self, request, user_id):
        try:
            user = Users.objects.get(user_id=user_id)
        except Users.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        
        history = History.objects.filter(user_id=user)
        serializer = HistorySerializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

# API to create a new user
class CreateUserAPIView(APIView):
    def post(self, request):
        data = request.data

        # Check if required fields are provided
        try:
            user_name = data['user_name']
            password = data['password']
            email = data['email']
        except KeyError:
            return Response({"error": "Invalid request. Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)

        # Validate password (no spaces allowed)
        if re.search(r'\s', password):
            return Response({"error": "Password cannot contain spaces."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Create the user
            user = Users.objects.create(
                user_name=user_name,
                password=make_password(password),
                email=email
            )
            return Response({"message": "User created successfully", "user_id": user.user_id}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# API to create a new question
class CreateQuestionAPIView(APIView):
    def post(self, request):
        data = request.data
        try:
            question = Questions.objects.create(
                ques_title=data['ques_title'],
                ques_detail=data['ques_detail'],
                ques_option=data['ques_option'],
                ques_answer=data['ques_answer']
            )
            return Response({"message": "Question created successfully", "ques_id": question.ques_id}, status=status.HTTP_201_CREATED)
        except KeyError:
            return Response({"error": "Invalid request. Missing required fields."}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"An error occurred: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

# Created a default home-page
class HomeView(View):
    def get(self, request):
        return HttpResponse("<h1>Welcome to QuizBit</h1>")