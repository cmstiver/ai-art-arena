# Generated by Django 4.1.7 on 2023-03-06 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIArtArena', '0007_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(default='ecb34a4d4e044ce5b0af2e299352a3bb', editable=False, primary_key=True, serialize=False),
        ),
    ]
