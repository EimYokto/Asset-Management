from django.shortcuts import render , redirect
from egatapp.models import *
from tablib import Dataset
from egatapp.resources import *
# Create your pages.
from django import template
from django.http import HttpResponse, HttpResponseRedirect ,FileResponse
import os
from django.template import loader
from django.urls import reverse
#Sending Emails
from django.views import View
from django.core.mail import EmailMessage
from django.conf import settings
from .forms import EmailForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required(login_url="/login/")
def index(request):
    num_Hardware = Hardware.objects.count()
    num_Software = Software.objects.count()
    num_People = People.objects.count()
    num_Information = Information.objects.count()
    num_In_house_service = In_house_service.objects.count()
    num_External_service = External_service.objects.count()

    Historys = History.objects.all()
    

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(
        {'num_Hardware':num_Hardware,
        'num_Software': num_Software,
        'num_People': num_People,
        'num_Information': num_Information,
        'num_Information': num_Information,
        'num_In_house_service':num_In_house_service,
        'num_External_service':num_External_service,
        'Historys':Historys,
        'segment': 'index'}, request))

@login_required(login_url="/login/")
def profile(request):
    context = {'segment': 'profile'}

    html_template = loader.get_template('home/profile.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def form(request):
    context = {'segment': 'form'}
    
    html_template = loader.get_template('Request_for_Change_Generation/form.html')
    return HttpResponse(html_template.render(context, request))



#Sending Emails
class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'Request_for_Change_Generation/email.html'
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        
        return render(request, self.template_name, {'email_form': form,'segment': 'email'})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            files = request.FILES.getlist('attach')
            
            mail = EmailMessage(subject, message, 'eimyoktoadmin@email.com', [email])
            try:
                for f in files:
                    mail.attach(f.name, f.read(), f.content_type)
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

            return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})

#class EmailAttachementView(View):
#   form_class = EmailForm
#    template_name = 'Request_for Change_Generation/email.html'

#    def get(self, request, *args, **kwargs):
#       form = self.form_class()
#        return render(request, self.template_name, {'email_form': form})

#    def post(self, request, *args, **kwargs):
#        form = self.form_class(request.POST, request.FILES)

#        if form.is_valid():
            
#            subject = form.cleaned_data['subject']
#            message = form.cleaned_data['message']
#            email = form.cleaned_data['email']
#            files = request.FILES.getlist('attach')

#            mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [email])
#            for f in files:
#                mail.attach(f.name, f.read(), f.content_type)
#            mail.send()
#            return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})

#        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})


def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        return redirect("/")







