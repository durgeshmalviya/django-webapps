# Generated by Django 4.2.6 on 2023-10-21 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WEBAPP', '0003_alter_tutorial_options_delete_customuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='image_url',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
