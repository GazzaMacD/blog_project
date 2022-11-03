# Generated by Django 4.1.2 on 2022-11-02 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
    ]

    operations = [
        migrations.CreateModel(
            name="StaffMember",
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
                    "name",
                    models.CharField(
                        help_text="Your name as you would like to read it on any material you produce for the site, blogs etc.",
                        max_length=70,
                    ),
                ),
                (
                    "bio",
                    models.TextField(
                        help_text="Tell the world what you would like them to know about you",
                        max_length=300,
                    ),
                ),
                (
                    "website",
                    models.URLField(
                        blank=True,
                        help_text="If your website fits in with this site, please add it's url. Subject to moderation",
                        max_length=100,
                    ),
                ),
                (
                    "twitter",
                    models.URLField(
                        blank=True,
                        help_text="If your twitter feed fits in with this site, please add it's url Subject to moderation",
                        max_length=100,
                    ),
                ),
                (
                    "instagram",
                    models.URLField(
                        blank=True,
                        help_text="If your instagram fits in with this site, please add it's url. Subject to moderation",
                        max_length=100,
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        blank=True,
                        help_text="If your linkedin fits in with this site, please add it's url. Subject to moderation",
                        max_length=100,
                    ),
                ),
                (
                    "profile_image",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="+",
                        to="wagtailimages.image",
                    ),
                ),
            ],
            options={
                "verbose_name": "Staff Member",
                "verbose_name_plural": "Staff Members",
            },
        ),
    ]