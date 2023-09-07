# Generated by Django 4.2.4 on 2023-09-06 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_post_image_remove_post_popularity_score_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcomment',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default=None, max_length='250', null=True, upload_to='blogposts/'),
        ),
    ]
