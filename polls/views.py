from django.http import HttpResponse
from .models import Question
import datetime


def index(request):
    question = Question(question_text="This is a new one", pub_date=datetime.datetime.now())
    question.save()
    questions = Question.objects.all()
    text = ""
    for question in questions:
        text += f"{question.question_text}\n"
    return HttpResponse(text)

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)