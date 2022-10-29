from django.db import models
from django.core.validators import MinValueValidator


class Musician(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Composition(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Album(models.Model):
    musician = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ('year', 'name')
        unique_together = ('musician', 'name')

    def __str__(self):
        return f'{self.name}, {self.year}'


class AlbumComposition(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='album_compositions')
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE, related_name='composition_albums')
    song_number = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    class Meta:
        ordering = ('song_number', 'composition__name')
        unique_together = (('album', 'composition'), ('album', 'song_number'))
