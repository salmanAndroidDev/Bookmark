from django import forms
from urllib import request
from django.core.files.base import ContentFile
from django.utils.text import slugify

from images.models import Image


class ImageCreateForm(forms.ModelForm):
    """Form class to create new Image"""

    class Meta:
        model = Image
        fields = ('title', 'url', 'description')
        widgets = {'url': forms.HiddenInput}

    def clean_url(self):
        """Validate that url must be JPEG"""
        url = self.cleaned_data['url']
        valid_extensions = ['jpg', 'jpeg']
        extension = url.split('.')[-1].lower()
        if extension not in valid_extensions:
            raise forms.ValidationError('The given URL is not a JPEG file')
        return url

    def save(self, force_insert=False,
             force_update=False,
             commit=True):
        """Downloading and saving image"""
        image = super().save(commit=False)
        image_url = self.cleaned_data['url']
        name = slugify(image.title)
        extension = image_url.split('.')[-1].lower()
        image_name = f'{name}.{extension}'

        #  download image from the given URL
        response = request.urlopen(image_url)
        image.image.save(image_name,
                         ContentFile(response.read()),
                         save=False)
        if commit:
            image.save()
        return image
