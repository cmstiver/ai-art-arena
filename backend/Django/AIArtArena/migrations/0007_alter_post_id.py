# Generated by Django 4.1.7 on 2023-03-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIArtArena', '0006_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='90357b5f4f564e06878678acae041e3d', editable=False, primary_key=True, serialize=False),
        ),
    ]
