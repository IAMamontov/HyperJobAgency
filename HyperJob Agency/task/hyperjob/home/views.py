from django.shortcuts import render
from django.views import View
from vacancy.models import Vacancy
from resume.models import Resume
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
# Create your views here.




class MyHomeView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            curuser = User.objects.get(username=request.user)
            if curuser.is_staff:
                return render(request, template_name="home.html", context={'content': Vacancy.objects.filter(author_id=curuser.id)})
            else:
                return render(request, template_name="home.html", context={'content': Resume.objects.filter(author_id=curuser.id)})
        else:
            return redirect('/login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            curuser=User.objects.get(username=request.user)
            if curuser.is_staff:
                return redirect('vacancy/new')
            else:
                return redirect('resume/new')
        else:
            return HttpResponseForbidden("Not Authorized")

