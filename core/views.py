from .models import Projects, Skills, Formation, Exp
from django.conf import settings
# Create your views here.

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect


# def home(request):
#     projects = Projects.objects.all()
#     skills = Skills.objects.all()
#     formation = Formation.objects.all()
#     exp = Exp.objects.all()

#     if request.method == 'GET':
#         form = ContactForm()
#     else:
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             from_email = form.cleaned_data['from_email']
#             subject = form.cleaned_data['subject']
#             message = form.cleaned_data['message']
#             try:
#                 send_mail(subject, message, from_email, [settings.DEFAULT_TO_EMAIL])
#             except BadHeaderError:
#                 return HttpResponse('Invalid header found.')
#             return redirect('contact_success')
            
#     ctx = {
#         "projects":projects,
#         "exp":exp,
#         "formation":formation,
#         "skills":skills,
#     }

#     return render(request, 'core/home.html', ctx)

# def project_view(request, project_slug):
#     project = get_object_or_404(Projects, slug=project_slug)
#     used_skill = Skills.objects.filter(projects=project)

#     ctx = {
#         "project":project,
#         "used_skill": used_skill,
#     }

#     return render(request, 'core/project_view.html', ctx)

# def skill_view(request, skill_slug):
#     skill = get_object_or_404(Skills, slug=skill_slug)
#     projects = Projects.objects.filter(skills=skill)

#     ctx = {
#         "skill":skill,
#         "projects":projects,        
#     }
#     return render(request, 'core/skill_view.html', ctx)


# # def contactView(request):
# #     if request.method == 'GET':
# #         form = ContactForm()
# #     else:
# #         form = ContactForm(request.POST)
# #         if form.is_valid():
# #             from_email = form.cleaned_data['from_email']
# #             subject = form.cleaned_data['subject']
# #             message = form.cleaned_data['message']
# #             try:
# #                 send_mail(subject, message, from_email, [settings.DEFAULT_TO_EMAIL])
# #             except BadHeaderError:
# #                 return HttpResponse('Invalid header found.')
# #             return redirect('contact_success')
   
# #     return render(request, "core/contact.html", {'form': form})


# # def contact_success(request):
# #     return render(request, "core/contact_success.html")
