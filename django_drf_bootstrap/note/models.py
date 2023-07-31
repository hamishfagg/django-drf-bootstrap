# Core
from django.db import models

from ..user.models import User

class Note(models.Model):

    id = models.BigAutoField(auto_created=True, primary_key=True, verbose_name='ID')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.TextField(null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
