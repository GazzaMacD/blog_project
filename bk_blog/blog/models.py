from django.db import models
from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.api import APIField
from wagtail.core.fields import StreamField

from streams import blocks


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

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog List Page"


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
    content = StreamField(
        [
            ("text_block", blocks.TextBlock()),
            ("full_width_image", blocks.FullWidthImage()),
        ],
        use_json_field=True,
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
        ),
        MultiFieldPanel(
            [
                InlinePanel("blog_categories", label="Category", min_num=1, max_num=4),
            ],
            heading="Blog Categories",
        ),
        FieldPanel("content"),
        MultiFieldPanel(
            [
                InlinePanel("blog_authors", label="Author", min_num=1, max_num=3),
            ],
            heading="Blog Authors",
        ),
        MultiFieldPanel(
            [
                InlinePanel("related_blog_posts", label="Related Post", max_num=4),
            ],
            heading="Related Blog Posts",
        ),
    ]

    api_fields = [
        APIField("editable_title"),
        APIField("intro"),
        APIField("top_image"),
        APIField("published_date"),
        APIField("blog_categories"),
        APIField("content"),
        APIField("blog_authors"),
    ]

    # Page limitations
    parent_page_type = ["blog.BlogIndexPage"]
    subpage_types = []

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog Post"
        verbose_name_plural = "Blog Posts"


class BlogAuthorOrderable(Orderable):
    page = ParentalKey(
        BlogDetailPage, on_delete=models.CASCADE, related_name="blog_authors"
    )
    author = models.ForeignKey("staff.StaffMember", on_delete=models.CASCADE)

    panels = [FieldPanel("author")]

    api_fields = [
        APIField("author"),
    ]


class BlogRelatedPostsOrderable(Orderable):
    page = ParentalKey(
        BlogDetailPage, on_delete=models.CASCADE, related_name="related_blog_posts"
    )
    blog_post = models.ForeignKey("blog.BlogDetailPage", on_delete=models.CASCADE)

    panels = [FieldPanel("blog_post")]

    api_fields = [
        APIField("blog_post"),
    ]


class BlogCategoryOrderable(Orderable):
    page = ParentalKey(
        BlogDetailPage, on_delete=models.CASCADE, related_name="blog_categories"
    )
    category = models.ForeignKey("snippets.ContentCategory", on_delete=models.CASCADE)

    panels = [FieldPanel("category")]

    api_fields = [
        APIField("category"),
    ]
