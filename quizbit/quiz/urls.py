# quiz/urls.py
from django.urls import path
from .views import QuestionListView, QuestionDetailView, SubmitAnswerView, UserHistoryView, CreateUserAPIView, CreateQuestionAPIView
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view() , name='home'),
    path('questions/', QuestionListView.as_view(), name='question-list'),
    path('questions/<int:ques_id>/', QuestionDetailView.as_view(), name='question-detail'),
    path('submit-answer/', SubmitAnswerView.as_view(), name='submit-answer'),
    path('user-history/<int:user_id>/', UserHistoryView.as_view(), name='user-history'),
    path('users/create/', CreateUserAPIView.as_view(), name='create-user'),
    path('questions/create/', CreateQuestionAPIView.as_view(), name='create-question'),
]
