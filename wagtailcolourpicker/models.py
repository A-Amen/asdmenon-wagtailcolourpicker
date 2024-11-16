from django.db import models
from colorfield.fields import ColorField
from wagtail.snippets.models import register_snippet

@register_snippet
class Color(models.Model):
    color_name = models.CharField(max_length=255, null=True)
    color = ColorField()

    def __str__(self) -> str:
        return self.color_name