# Generated by Django 4.1.7 on 2023-03-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIArtArena', '0010_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.CharField(editable=False, max_length=32, primary_key=True, serialize=False),
        ),
    ]