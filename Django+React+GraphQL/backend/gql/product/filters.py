from django.db.models import Q
import django_filters
from ChoLon.models import ProductModel

class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method = 'filter-search')

    class Meta:
        model = ProductModel
        fields = ()

    def filter_search(self, queryset, name, value):
        return queryset_filter(
            Q(pName__icontains = value) | Q(pDesc__icontains = value)
        )
