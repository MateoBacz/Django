from django.http import HttpResponse

# def index(request):
#     pytania=Question.objects.all()
#     return HttpResponse(pytania)

from django.http import HttpResponse, Http404
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404


def index(request):
    # pytania = Question.objects.all().order_by('-pub_date')[:5]
    # response = "<html><ul>"
    # for pytanie in pytania:
    #     response += f"<li>{pytanie.question_text}</li>"
    # response += "</ul></html>"

    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {'question':question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    choice_id = request.POST['choice']
    print("choice_id: " + str(choice_id))
    print("question_id: " + str(question_id))

    q = Question.objects.get(pk=question_id)
    print(q.question_text)

    odp = Choice.objects.get(pk=choice_id)
    #odp.vote()
    print(f"Odp: {odp.choice_text}, głosów: {odp.votes} ")

    return HttpResponse("You're voting on question %s." % question_id)

