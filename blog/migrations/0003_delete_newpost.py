# Generated by Django 2.1.3 on 2018-11-25 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_newpost'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NewPost',
        ),
    ]
