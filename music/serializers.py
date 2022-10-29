from rest_framework import serializers

from .models import Composition, Album, Musician, AlbumComposition


class CompositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Composition
        fields = ('pk', 'name')


class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = ('pk', 'name')


class AlbumCompositionSerializer(serializers.ModelSerializer):
    composition = serializers.StringRelatedField()
    album = serializers.StringRelatedField()

    class Meta:
        model = AlbumComposition
        fields = ('pk', 'composition', 'album', 'song_number')


class CreateUpdateAlbumCompositionSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        if AlbumComposition.objects.filter(composition=attrs['composition']).exclude(
            album__musician=attrs['album'].musician
        ).exists():
            raise serializers.ValidationError("This composition cannot be added to another musician's album.")

        return attrs

    class Meta:
        model = AlbumComposition
        fields = ('pk', 'composition', 'album', 'song_number')


class AlbumNestedAlbumCompositionSerializer(serializers.ModelSerializer):
    composition = serializers.StringRelatedField()

    class Meta:
        model = AlbumComposition
        fields = ('pk', 'composition', 'song_number')


class AlbumSerializer(serializers.ModelSerializer):
    album_compositions = AlbumNestedAlbumCompositionSerializer(many=True, read_only=True)
    musician = serializers.StringRelatedField()

    class Meta:
        model = Album
        fields = ('pk', 'name', 'year', 'musician', 'album_compositions')


class CreateUpdateAlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('pk', 'name', 'year', 'musician')
