import os

from django.db import models
from django.urls import reverse, reverse_lazy


class Notice(models.Model):
    title = models.CharField('제목', max_length=255)
    content = models.TextField('내용', )
    file = models.FileField(upload_to='notice/%Y/%m/%d')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse_lazy('c_notice_detail', kwargs={'pk': self.pk})

    def get_file_name(self):
        return os.path.basename(self.file.name)