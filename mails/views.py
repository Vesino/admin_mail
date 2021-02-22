from django.shortcuts import render, reverse
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView

# Models
from .models import Mail

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