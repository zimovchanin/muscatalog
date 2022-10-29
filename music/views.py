from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from muscatalog.views import SerializerByActionMixin

from .serializers import (
    CompositionSerializer, AlbumSerializer, AlbumCompositionSerializer, MusicianSerializer, CreateUpdateAlbumSerializer,
    CreateUpdateAlbumCompositionSerializer
)
from .models import Composition, Album, AlbumComposition, Musician
from .filters import CompositionFilterSet, AlbumFilterSet


class CompositionViewSet(viewsets.ModelViewSet):
    """This API allows to create/update/delete/show composition."""
    queryset = Composition.objects.all()
    serializer_class = CompositionSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompositionFilterSet


class AlbumViewSet(SerializerByActionMixin, viewsets.ModelViewSet):
    """This API allows to create/update/delete/show album for musicians."""
    queryset = Album.objects.all().select_related('musician').prefetch_related('album_compositions__composition')
    serializer_class = AlbumSerializer
    action_serializer_map = {
        'create': CreateUpdateAlbumSerializer,
        'update': CreateUpdateAlbumSerializer,
        'partial_update': CreateUpdateAlbumSerializer,
    }
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AlbumFilterSet


class AlbumCompositionViewSet(SerializerByActionMixin, viewsets.ModelViewSet):
    """This API allows to add/update/delete/show composition to the album."""
    queryset = AlbumComposition.objects.all().select_related('composition', 'album')
    serializer_class = AlbumCompositionSerializer
    action_serializer_map = {
        'create': CreateUpdateAlbumCompositionSerializer,
        'update': CreateUpdateAlbumCompositionSerializer,
        'partial_update': CreateUpdateAlbumCompositionSerializer,
    }


class MusicianViewSet(viewsets.ModelViewSet):
    """This API allows to create/update/delete/show musician."""
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
