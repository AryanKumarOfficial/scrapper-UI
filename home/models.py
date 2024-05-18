from django.db import models
import io
import numpy as np


class URLModel(models.Model):
    url = models.URLField(max_length=1000)
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.URLField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


class scrappedDataModel(models.Model):
    url = models.URLField(max_length=1000)
    words_collection = models.BinaryField()
    unique_words_count = models.IntegerField()
    total_words_count = models.IntegerField()
    title = models.CharField(max_length=1000)
    total_reviews = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url


def set_word_collection(self, words_collection):
    out = io.BytesIO()
    np.save(out, words_collection)
    out.seek(0)
    self.words_collection = out.read()


def get_word_collection(self):
    inp = io.BytesIO(self.words_collection)
    inp.seek(0)
    return np.load(inp)