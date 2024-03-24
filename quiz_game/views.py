from django.shortcuts import render
from .models import Question
from django.http import HttpResponse

def quiz_view(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'quiz.html', context)

def evaluate_answer(request):
    if request.method == 'POST':
        user_answers = request.POST.copy()
        csrf_token = user_answers.pop('csrfmiddlewaretoken', None) 
        score = 0
        for question_id, choice_id in user_answers.items():
            question = Question.objects.get(pk=question_id)
            if question.answer.correct_choice_id == int(choice_id):
                score += 1
        total_questions = Question.objects.count()
        context = {'score': score, 'total_questions': total_questions}
        return render(request, 'quiz_result.html', context)
    else:
        return HttpResponse("Method not allowed", status=405)
