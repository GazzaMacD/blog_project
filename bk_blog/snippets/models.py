from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.snippets.models import register_snippet
from wagtail.api import APIField

# Create your models here.
@register_snippet
class ContentCategory(models.Model):
    """Snippet model for content categories to be use on various models across app"""

    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text="Max length is 100 characters",
    )
    slug = models.SlugField(
        max_length=150,
        null=False,
        blank=False,
        unique=True,
        help_text="Max length is 150. Slugs should be all lower case separated by hypens. Must be unique.",
    )

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    api_fields = [
        APIField("name"),
        APIField("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Content Category"
        verbose_name_plural = "Content Categories"
        ordering = [
            "name",
        ]
