# Generated by Django 4.1.2 on 2022-11-02 17:43

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("staff", "0002_remove_staffmember_id_staffmember_page_ptr"),
        ("blog", "0004_alter_blogdetailpage_content"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="blogdetailpage",
            options={"verbose_name": "Blog Post", "verbose_name_plural": "Blog Posts"},
        ),
        migrations.CreateModel(
            name="BlogAuthorOrderable",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "sort_order",
                    models.IntegerField(blank=True, editable=False, null=True),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="staff.staffmember",
                    ),
                ),
                (
                    "page",
                    modelcluster.fields.ParentalKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="blog_authors",
                        to="blog.blogdetailpage",
                    ),
                ),
            ],
            options={
                "ordering": ["sort_order"],
                "abstract": False,
            },
        ),
    ]