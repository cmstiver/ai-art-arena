# Generated by Django 4.1.7 on 2023-03-06 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIArtArena', '0002_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='e10e0b98e61d4dedbaa47023ff4e6612', editable=False, primary_key=True, serialize=False),
        ),
    ]