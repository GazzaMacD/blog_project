from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField


class HomePage(Page):
    banner_title = models.CharField(max_length=100, blank=False, null=False)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
    ]

    api_fields = [
        APIField("banner_title"),
    ]
    max_count = 1
    parent_page_type = ["wagtailcore.Page"]
