from django.db import models


class UrlInfo(models.Model):
    url_id = models.BigIntegerField(primary_key=True, null=False, unique=True)
    short_url = models.CharField(max_length=20, null=False)
    long_url = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
