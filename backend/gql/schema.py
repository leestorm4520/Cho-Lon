from graphene import List, Field, Argument, ID, ObjectType, Schema
from graphene_django.filter import DjangoFilterConnectionField
from django.db.models import Q
import django_filters
from types import UserType, ProductType
from .ChoLon.models import UserModel, ProductModel


class Query(ObjectType):
    users = List(UserType)
    product = Field(ProductType, id = Argument(ID, required =True))
    products = DjangoFilterConnectionField(ProductType, filterset_class = ProductFilter())

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_note(root, info, **kwargs):
        return ProductModel.objects.get(id = kwargs.get('id'))

    def resolve_notes(root, info, **kwargs):
        return ProductModel.objects.all()

class ProductFilter(django_filters.FilterSet):
    search = django_filters.CharFilter(method = 'filter-search')

    class Meta:
        model = ProductModel
        fields = ()

    def filter_search(self, queryset, name, value):
        return queryset_filter(
            Q(pName__icontains == value) | Q(pDesc__icontains = value)
        )


schema = Schema(query = Query)

