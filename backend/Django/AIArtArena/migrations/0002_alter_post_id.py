# Generated by Django 4.1.7 on 2023-03-06 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIArtArena', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='ee1aaaf961674860b2fb1be7f33f2e31', editable=False, primary_key=True, serialize=False),
        ),
    ]
