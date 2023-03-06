from django.db import models
from craiyon import Craiyon
import uuid
import base64
from django.core.files.base import ContentFile


class Post(models.Model):
    id = models.CharField(primary_key=True, max_length=32, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
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
        if not self.id:
            self.id = uuid.uuid4().hex

        generator = Craiyon()
        result = generator.generate(self.title)
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
