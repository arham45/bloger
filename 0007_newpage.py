# Generated by Django 4.2.4 on 2023-09-07 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_delete_newpage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
    ]
