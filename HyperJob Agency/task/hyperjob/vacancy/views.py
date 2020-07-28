from django.views import View
from django.shortcuts import render
from vacancy.models import Vacancy
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.models import User


# Create your views here.

class VacancyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "vacancy.html", context={'vacancies': Vacancy.objects.all()})

class NewVacancyView(View):

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            curuser=User.objects.get(username=request.user)
            if curuser.is_staff:
                return render(request, "new.html", context={'content_type': "vacancy"})
            else:
                return HttpResponseForbidden("Not Authorized")
        else:
            return HttpResponseForbidden("Not Authorized")

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            curuser=User.objects.get(username=request.user)
            if curuser.is_staff:
                author = request.user
                description = request.POST.get('description')
                new_Vacancy = Vacancy.objects.create(author=author, description=description)
                return redirect('/home')
            else:
                return HttpResponseForbidden("Not Authorized")
        else:
            return HttpResponseForbidden("Not Authorized")
