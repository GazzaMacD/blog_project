from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from .models import BlogDetailPage


class BlogDetailAdmin(ModelAdmin):
    model = BlogDetailPage
    list_display = ("title", "published_date")
    menu_order = 200


modeladmin_register(BlogDetailAdmin)
