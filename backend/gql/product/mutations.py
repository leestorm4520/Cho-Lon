from graphene import Boolean, Field, ID, InputObjectType, Mutation, String, Int
from rest_framework import serializers
from ChoLon.models import ProductModel
from gql.types import ProductType

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = (
            'id',
            'pName',
            'pPrice',
            'pQuantity',
            'pDesc',
        )
class ProductInputType(InputObjectType):
    pName = String()
    pPrice = String()
    pQuantity = String()
    pDesc = String()

class ProductCreate(Mutation):
    class Arguments:
        input = ProductInputType(required = True)
    product = Field(ProductType)

    @classmethod
    def mutate(cls, root, info, **data):
        serializer = ProductSerializer(data = data.get('input'))
        serializer.is_valid(raise_exception = True)

        return ProductCreate(product = serializer.save())

class ProductDelete(Mutation):
    class Arguments:
        id = ID(required = True)

    ok = Boolean()
    @classmethod
    def mutate(cls, root, info, **data):
        product = ProductModel.objects.get(id = data.get('id'))
        product.delete()

        return ProductDelete(ok = True)
