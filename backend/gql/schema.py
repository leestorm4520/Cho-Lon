from graphene import List, Field, Argument, ID, ObjectType, Schema
from graphene_django.filter import DjangoFilterConnectionField
from .types import UserType, ProductType
from ChoLon.models import UserModel, ProductModel
from .product.mutations import ProductCreate, ProductDelete
from .product.filters import ProductFilter
from .user.mutations import UserCreate, UserDelete
from .user.filters import UserFillter

class Query(ObjectType):
    user = Field(UserType, id = Argument(ID, required = True))
    users = DjangoFilterConnectionField(UserType, filterset_class = UserFilter)
    product = Field(ProductType, id = Argument(ID, required = True))
    products = DjangoFilterConnectionField(ProductType, filterset_class = ProductFilter)

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_note(root, info, **kwargs):
        return ProductModel.objects.get(id = kwargs.get('id'))

    def resolve_notes(root, info, **kwargs):
        return ProductModel.objects.all()

class Mutation(ObjectType):
    product_create = ProductCreate.Field()
    product_delete = ProductDelete.Field()
    user_create = UserCreate.Field()
    user_delete = UserDelete.Field()


schema = Schema(query = Query, mutation = Mutation)

