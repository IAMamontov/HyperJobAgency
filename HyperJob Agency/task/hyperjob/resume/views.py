from django.views import View
from django.shortcuts import render
from resume.models import Resume
from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.contrib.auth.models import User

# Create your views here.

class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "resume.html", context={'resumes': Resume.objects.all()})


class NewResumeView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "new.html", context={'content_type': "resume"})

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            #curuser=User.objects.get(username=request.user)
            author = request.user
            description = request.POST.get('description')
            new_Resume = Resume.objects.create(author=author, description=description)
            return redirect('/home')
        else:
            return HttpResponseForbidden("Not Authorized")