from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.api import APIField
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    banner_title = models.CharField(max_length=100, blank=False, null=False)
    banner_intro = models.TextField(max_length=250, blank=False, null=False)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_intro"),
                FieldPanel("banner_image"),
            ],
            heading="Home Top Banner",
        )
    ]

    api_fields = [
        APIField("banner_title"),
        APIField("banner_intro"),
        APIField("banner_image"),
    ]
    # Page limitations in admin panel
    max_count = 1
    parent_page_type = ["wagtailcore.Page"]
    subpage_types = ["blog.BlogIndexPage"]
