# Generated by Django 4.1.7 on 2023-03-06 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIArtArena', '0005_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='3d4667b2059941c38d0f834795f00a32', editable=False, primary_key=True, serialize=False),
        ),
    ]