# Generated by Django 5.1 on 2024-08-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("odisea", "0005_article_created_at_article_likes_comment_created_at_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="slug",
            field=models.CharField(default="slug1", max_length=150),
            preserve_default=False,
        ),
    ]
