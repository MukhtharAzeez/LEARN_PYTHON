from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.template import loader

from polls.models import Question


def index(request):
    # latest_question_list = Question.objects.order_by("-pub_date")[:5]
    # output = [q.question_text for q in latest_question_list]
    # output = ", ".join(output)
    # output = ", ".join([q.question_text for q in latest_question_list])
    # return HttpResponse(output)
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # Way to find results that match to a specific id
    # output = Question.objects.get(pk=question_id)

    # Way to find results that match to a specific id like above, but here we use get_object_or_404 to catch the error (django shortcut)
    output = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"details": output})


def results(request, question_id):
    # Used try and except to catch the 404 error
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/results.html", {"question": question})


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)