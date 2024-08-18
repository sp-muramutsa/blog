# Generated by Django 5.0.7 on 2024-07-23 20:27

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("odisea", "0004_alter_article_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="article",
            name="likes",
            field=models.ManyToManyField(
                blank=True, related_name="liked_posts", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reader",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="reader",
            name="following",
            field=models.ManyToManyField(
                blank=True, related_name="followers", to="odisea.author"
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="title",
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name="article",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="reader",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
