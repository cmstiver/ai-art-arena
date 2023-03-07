from django.db import models
from craiyon import Craiyon
import uuid
import base64
from django.core.files.base import ContentFile
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=32, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=70, default="")
    prompt = models.CharField(max_length=500)
    owner = models.ForeignKey(
        'auth.User', related_name='posts', on_delete=models.CASCADE, editable=False)
    liked_by = models.ManyToManyField(
        User, related_name='post_like', editable=False)
    is_private = models.BooleanField(default=True)
    image0 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image1 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image2 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image3 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image4 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image5 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image6 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image7 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)
    image8 = models.ImageField(
        upload_to='images/', null=True, blank=True, editable=False)

    def save(self, *args, **kwargs):
        is_new_instance = not self.pk

        if is_new_instance:
            self.id = uuid.uuid4().hex

            self._meta.get_field('prompt').editable = False

            generator = Craiyon()
            result = generator.generate(self.prompt)
            images = result.images
            counter = 0
            for i in images:
                image = base64.decodebytes(i.encode("utf-8"))
                if counter == 0:
                    self.image0.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 1:
                    self.image1.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 2:
                    self.image2.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 3:
                    self.image3.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 4:
                    self.image4.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 5:
                    self.image5.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 6:
                    self.image6.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 7:
                    self.image7.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                elif counter == 8:
                    self.image8.save(f'{self.id}_{counter}.jpg',
                                     ContentFile(image), save=False)
                counter += 1
        super().save(*args, **kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
