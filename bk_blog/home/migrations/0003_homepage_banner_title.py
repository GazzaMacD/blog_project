# Generated by Django 4.1.2 on 2022-10-26 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_create_homepage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="banner_title",
            field=models.CharField(default="", max_length=100),
            preserve_default=False,
        ),
    ]
