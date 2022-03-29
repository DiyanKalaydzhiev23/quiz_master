from django.urls import path
from quiz_master.quiz_app.views import QuizzesView, AddQuizView

urlpatterns = [
    path('quizzes/', QuizzesView.as_view(), name='quizzes'),
    path('add-quiz/', AddQuizView.as_view(), name='add quiz'),
]
