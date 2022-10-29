from django_filters import FilterSet, filters

from .models import Composition, Album


class CompositionFilterSet(FilterSet):
    musician = filters.NumberFilter(method='filter_musician')

    def filter_musician(self, queryset, name, value):
        return queryset.filter(composition_albums__album__musician=value).distinct()

    class Meta:
        model = Composition
        fields = ('musician',)


class AlbumFilterSet(FilterSet):
    year = filters.NumericRangeFilter()

    class Meta:
        model = Album
        fields = ('musician', 'year')
