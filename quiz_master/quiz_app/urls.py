from django.urls import path
from quiz_master.quiz_app.views import AddQuizView, EditQuizView, DeleteQuizView, LandingView, \
    SolveQuizView, quizzes_view


urlpatterns = [
    path('', LandingView.as_view(), name='home'),
    path('quizzes/', quizzes_view, name='quizzes'),
    path('solve/<int:pk>', SolveQuizView.as_view(), name='solve quiz'),
    path('add-quiz/', AddQuizView.as_view(), name='add quiz'),
    path('edit-quiz/<int:pk>', EditQuizView.as_view(), name='edit quiz'),
    path('delete-quiz/<int:pk>', DeleteQuizView.as_view(), name='delete quiz'),
]
