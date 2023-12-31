# Generated by Django 4.2.4 on 2023-09-06 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.RemoveField(
            model_name='post',
            name='popularity_score',
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='image',
            field=models.FileField(default=None, max_length='250', null=True, upload_to='blogposts/'),
        ),
    ]
