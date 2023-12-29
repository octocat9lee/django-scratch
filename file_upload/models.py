from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='uploads/', null=True)
    upload_method = models.CharField(max_length=20, verbose_name="Upload Method")
