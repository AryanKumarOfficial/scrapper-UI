from django.db import models


class ScrapFormModel(models.Model):
    url = models.URLField(max_length=1000)

    class Meta:
        verbose_name = 'ScrapFormModel'
        verbose_name_plural = 'ScrapFormModels'

    def __str__(self):
        return self.url
