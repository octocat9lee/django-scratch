from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/', null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
