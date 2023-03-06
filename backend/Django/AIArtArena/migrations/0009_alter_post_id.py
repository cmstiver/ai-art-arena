# Generated by Django 4.1.7 on 2023-03-06 09:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('AIArtArena', '0008_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]