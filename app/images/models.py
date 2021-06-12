from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify


class Image(models.Model):
    """Image model"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='images_created',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,
                            blank=True)
    url = models.URLField()
    image = models.ImageField(upload_to='images/%y/%m/%d/')
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True,
                                   db_index=True)

    users_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        related_name='images_liked',
                                        blank=True)

    def save(self, *args, **kwargs):
        """Generate slug field automatically, if not provided"""
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        """Canonical url of image file"""
        return reverse('images:detail', args=[self.id, self.slug])

    def __str__(self):
        return self.title
