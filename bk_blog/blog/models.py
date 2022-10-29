from re import I
from unittest.util import _MAX_LENGTH
from django.db import models
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.api import APIField


class BlogIndexPage(Page):
    top_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )
    intro = models.TextField(max_length=250, blank=False, null=False)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("top_image"),
                FieldPanel("intro"),
            ],
            heading="Blog List Page Header Area",
        )
    ]

    api_fields = [
        APIField("intro"),
        APIField("top_image"),
    ]
    # Page limitations
    max_count = 1
    parent_page_type = ["home.HomePage"]
    subpage_types = ["blog.BlogDetailPage"]


class BlogDetailPage(Page):
    editable_title = models.TextField(
        max_length=50,
        null=False,
        blank=False,
        help_text="Max length 50. This is the title to be used on the frontend. White space and line breaks will show in designs.",
    )
    intro = models.TextField(
        max_length=250,
        blank=False,
        null=False,
        help_text="The maxi length is 250 characters",
    )
    top_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )
    published_date = models.DateTimeField(
        blank=False,
        null=False,
        help_text="IMPORTANT NOTE: This date will affect the order on list pages.",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("editable_title"),
                FieldPanel("intro"),
                FieldPanel("top_image"),
                FieldPanel("published_date"),
            ],
            heading="Blog Post Header Area",
        )
    ]

    api_fields = [
        APIField("editable_title"),
        APIField("intro"),
        APIField("top_image"),
        APIField("published_date"),
    ]

    # Page limitations
    parent_page_type = ["blog.BlogIndexPage"]
