from django.db import models

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
    schema = models.JSONField(default=schema_default, help_text="JSON schema")
    published = models.BooleanField(default=False, help_text="Use this schema?")
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # if is published, then set false in published field of other schemas
        # if not published and there aren't other schemas published set True in this schema
        super().save(*args, **kwargs)

    class Meta:
        get_latest_by = "created"
        ordering = ["-last_modified"]
        verbose_name = "Landing schema"
