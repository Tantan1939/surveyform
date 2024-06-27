from django.shortcuts import render
from surveyapp.questionnaires import questions, choices
from django.urls import reverse
from django.http import HttpResponseRedirect
from . models import Survey
from django.db import transaction


def Index(request):
    if request.method == "POST":
        selected_choices = {}
        for key in questions.keys():
            selected_choices[key] = request.POST.get(key)

        with transaction.atomic():
            Survey.objects.create(answers=selected_choices)

        return HttpResponseRedirect(reverse("app:success"))

    return render(request, "app/index.html", context={
        "questions": questions, "choices": choices
    })


def Success(request):
    return render(request, "app/thanks.html")
