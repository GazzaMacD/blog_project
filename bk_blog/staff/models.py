from django.db import models
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from wagtail.models import Page
from wagtail.api import APIField


class StaffListPage(Page):
    editable_title = models.TextField(
        max_length=50,
        null=False,
        blank=False,
        help_text="Max length 50. This is the title to be used on the frontend. White space and line breaks will show in designs.",
    )
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
                FieldPanel("editable_title"),
                FieldPanel("top_image"),
                FieldPanel("intro"),
            ],
            heading="Staff List",
        )
    ]

    api_fields = [
        APIField("editable_title"),
        APIField("intro"),
        APIField("top_image"),
    ]
    # Page limitations
    max_count = 1
    parent_page_type = ["home.HomePage"]
    subpage_types = ["staff.StaffMember"]

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog List Page"


class StaffMember(Page):
    """Model for all staff, creators etc"""

    name = models.CharField(
        max_length=70,
        null=False,
        blank=False,
        help_text="Your name as you would like to read it on any material you produce for the site, blogs etc.",
    )
    bio = models.TextField(
        max_length=300,
        null=False,
        blank=False,
        help_text="Tell the world what you would like them to know about you",
    )
    profile_image = models.ForeignKey(
        "wagtailimages.Image",
        on_delete=models.SET_NULL,
        blank=False,
        null=True,
        related_name="+",
    )
    website = models.URLField(
        max_length=100,
        null=False,
        blank=True,
        help_text="If your website fits in with this site, please add it's url. Subject to moderation",
    )
    twitter = models.URLField(
        max_length=100,
        null=False,
        blank=True,
        help_text="If your twitter feed fits in with this site, please add it's url Subject to moderation",
    )
    instagram = models.URLField(
        max_length=100,
        null=False,
        blank=True,
        help_text="If your instagram fits in with this site, please add it's url. Subject to moderation",
    )
    linkedin = models.URLField(
        max_length=100,
        null=False,
        blank=True,
        help_text="If your linkedin fits in with this site, please add it's url. Subject to moderation",
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel("name"),
                FieldPanel("profile_image"),
                FieldPanel("bio"),
            ],
            heading="Staff & Creator Details",
        ),
        MultiFieldPanel(
            [
                FieldPanel("website"),
                FieldPanel("twitter"),
                FieldPanel("instagram"),
                FieldPanel("linkedin"),
            ],
            heading="Links",
        ),
    ]

    api_fields = [
        APIField("name"),
        APIField("profile_image"),
        APIField("bio"),
        APIField("website"),
        APIField("twitter"),
        APIField("instagram"),
        APIField("linkedin"),
    ]

    parent_page_type = ["home.HomePage"]
    subpage_types = []

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Staff Member"
        verbose_name_plural = "Staff Members"
