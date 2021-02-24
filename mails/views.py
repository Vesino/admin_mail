# Django
from django.shortcuts import render, reverse, redirect
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.shortcuts import get_object_or_404
from django.utils import timezone

# Models
from .models import Mail
from user_mails.models import UserMail
from users.models import User

# Forms
from .forms import CreateMailForm

class MailListView(ListView):
    model = Mail
    template_name = 'mails/list.html'
    paginate_by = 10

class MailCreateView(CreateView):
    model = Mail
    template_name = 'mails/create.html'
    form_class = CreateMailForm

    def get_success_url(self):
        return reverse('mails:list')

class MailDeleteView(DeleteView):
    model = Mail
    success_url = reverse_lazy('mails:list')

class MailUpdateView(UpdateView):
    model = Mail
    form_class = CreateMailForm
    template_name = 'mails/update.html'

    def get_success_url(self):
        return reverse('mails:list')

class MailDetailView(DetailView):
    model = Mail
    template_name = 'mails/detail.html'


def create_mail(subject, user, template_path='', context={}):
    template = get_template(template_path)
    content = template.render(context)

    message = EmailMultiAlternatives(
        subject,
        'VesinoVargas',
        settings.EMAIL_HOST_USER,
        [user.email]
    )

    message.attach_alternative(content, 'text/html')
    return message

def send(request, pk):
    mail = get_object_or_404(Mail, pk=pk)

    for user in User.objects.filter(newsletter=True):
        user_mail = UserMail.objects.create(user=user, mail=mail)
        context = {
            'mail':mail,
            'user':user
        }
        email = create_mail(mail.subject, user, 'mails/base/base.html', context)
        email.send(fail_silently=False)
        user_mail.mail_sent_at = timezone.now()
        user_mail.save()
    
    return redirect('mails:detail', mail.id)