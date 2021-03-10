from django.db import models
from django.core.cache import cache


# Create your models here.
def schema_default():
    return {
        "hero": {
            "title": "edcilo.com",
            "subtitle": "Fullstack developer",
            "description": "Lorem ipsum dolor sit amet, consectetur idiapiscing"
        }
    }


class Landing(models.Model):
    name = models.CharField("Schema's name", max_length=100, unique=True)
    domain = models.CharField(max_length=100, default='127.0.0.1;localhost')
    schema = models.JSONField(default=schema_default, help_text="JSON schema")
    published = models.BooleanField(default=False, help_text="Use this schema?")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        cache.delete_pattern("*landing_view*")
        print(Landing.objects.filter(published=True, domain__contains=self.domain).exclude(id=self.id).count())

        if self.published is True:
            Landing.objects.filter(published=True, domain=self.domain).exclude(id=self.id).update(published=False)
        elif Landing.objects.filter(published=True, domain=self.domain).exclude(id=self.id).count() == 0:
            self.published = True

        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        cache.delete_pattern("*landing_view*")
        super(Landing, self).delete(using, keep_parents)

    class Meta:
        get_latest_by = "created"
        ordering = ["-last_modified"]
        verbose_name = "Landing schema"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    message = models.TextField(max_length=2048)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
