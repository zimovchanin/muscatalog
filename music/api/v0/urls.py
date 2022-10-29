from rest_framework import routers

from music.views import CompositionViewSet, AlbumViewSet, AlbumCompositionViewSet, MusicianViewSet


router = routers.SimpleRouter()
router.register('compositions', CompositionViewSet)
router.register('albums', AlbumViewSet)
router.register('album-compositions', AlbumCompositionViewSet)
router.register('musicians', MusicianViewSet)

urlpatterns = router.urls
