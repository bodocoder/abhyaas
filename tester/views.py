from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    tenq = Question.objects.order_by('-updated')[:10]
    # tenq = ', '.join([str(q) for q in tenq])
    context = {
        'tenq': tenq,
    }
    return render(request,'tester/index.html',context)
    # return HttpResponse("You have total 10 questions")

def result(request):
    params = dict(request.GET)
    score=0
    for key in params:
        try:
            if Question.objects.get(id=key).correctOption == params[key][0]:
                score += 1
        except:
            continue
    context = {
        'score' : score
    }
    return render(request,'tester/result.html',context)