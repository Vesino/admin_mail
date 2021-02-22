from django.db import models

# Models
from mails.models import Mail
from users.models import User

class UserMail(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mail = models.ForeignKey(Mail, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)
    token = models.CharField(max_length=100, null=True, blank=True)
    mail_sent_at = models.DateTimeField(default=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.mail.subject} - {self.user.username}"
