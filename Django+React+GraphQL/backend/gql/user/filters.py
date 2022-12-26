from django.db.models import Q
import django_filters
from ChoLon.models import UserModel

class UserFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method = 'filter-search')

    class Meta:
        model = UserModel
        fields = ()

    def filter_search(self, queryset, name, value):
        return queryset_filter(
            Q(email__icontains = value)
        )
