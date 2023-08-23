from django.db import models


class Images(models.Model):
    img = models.ImageField(upload_to='images', null=True, blank=True)
    Category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True, related_name='images')


class Category(models.Model):
    name = models.CharField(max_length=150)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Meta:
    verbose_name = 'Category'
    verbose_name_plural = 'Category'