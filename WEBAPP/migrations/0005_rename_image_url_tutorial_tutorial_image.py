# Generated by Django 4.2.6 on 2023-10-21 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0004_tutorial_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='image_url',
            new_name='tutorial_image',
        ),
    ]
