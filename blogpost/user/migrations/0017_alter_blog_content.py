# Generated by Django 4.2.7 on 2023-12-15 13:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(default=1),
            preserve_default=False,
        ),
    ]
