from graphene import List, Field, Argument, ID, ObjectType, Schema
from graphene_django import DjangoConnectionField
from types import UserType, ProductType
from .ChoLon.models import UserModel, ProductModel


class Query(graphene.ObjectType):
    users = List(UserType)
    product = Field(ProductType, id = Argument(ID, required =True))
    products = DjangoConnectionField(ProductType)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_note(root, info, **kwargs):
        return ProductModel.objects.get(id = kwargs.get('id'))

    def resolve_notes(root, info, **kwargs):
        return ProductModel.objects.all()

schema = Schema(query = Query)

