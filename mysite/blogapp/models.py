from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(null=True,blank=True)
    p_d = models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blogapp:detail_blog', kwargs={'pk': self.pk})