from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock as DefaultImageChooserBlock


class ImageChooserBlock(DefaultImageChooserBlock):
    def get_api_representation(self, value, context=None):
        if value:
            return {
                "id": value.id,
                "title": value.title,
                "original": value.get_rendition("original").attrs_dict,
                # "thumbnail": value.get_rendition("fill-120x120").attrs_dict, # use this if need thumbnail
            }


class TextBlock(blocks.RichTextBlock):
    def __init__(
        self,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.features = [
            "h3",
            "h4",
            "bold",
            "italic",
            "ol",
            "ul",
            "link",
            "hr",
            "blockquote",
        ]

        class Meta:
            icon = "pilcrow"
            label = "Text"


class FullWidthImage(blocks.StructBlock):
    """A full width image with an optional caption"""

    image = ImageChooserBlock(help_text="Use an image of 1280px x 720px")
    caption = blocks.CharBlock(
        max_length=40,
        required=False,
        help_text="Optional caption, max length = 40 characters",
    )

    class Meta:
        icon = "image"
        label = "Full Width Image"
