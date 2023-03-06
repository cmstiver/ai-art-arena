# Generated by Django 4.1.7 on 2023-03-06 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default='8b8f6550fe9c4fb8884d1600ce156f66', editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=500)),
                ('image0', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image1', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image4', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image5', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image6', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image7', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('image8', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
    ]