from django.urls import path
from .views import quiz_view, evaluate_answer

urlpatterns = [
    path('', quiz_view, name='quiz_view'),
    path('result/', evaluate_answer, name='result'),
]
