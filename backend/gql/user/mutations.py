from graphene import Boolean, Field, ID, InputObjectType, Mutation, String, Int
from rest_framework import serializers
from ChoLon.models import UserModel
from gql.types import UserType

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'id',
            'fName',
            'lName'
            'email',
        )
class UserInputType(InputObjectType):
    fName = String()
    lName = String()
    email = String()

class UserCreate(Mutation):
    class Arguments:
        input = UserInputType(required = True)
    user = Field(UserType)

    def mutate(cls, root, info, **data):
        serializer = UserSerializer(data = data.get('input'))
        serializer.is_valid(raise_exception = True)

        return UserCreate(product = serializer.save())

class UserDelete(Mutation):
    class Arguments:
        id = ID(required = True)

        ok = Boolean()

    def mutate(cls, root, info, **data):
        product = UserModel.objects.get(id = data.get('id'))
        product.delete()

        return UserDelete(ok = True)



# class CreateUser(graphene.Mutation):
#     id = graphene.Int()
#     first_name = graphene.String()
#     last_name = graphene.String()
#     email = graphene.String()
#     address = graphene.String()
#     phone_number = graphene.String()

#     class Arguments:
#         first_name = graphene.String()
#         last_name = graphene.String()
#         email = graphene.String()
#         address = graphene.String()
#         phone_number = graphene.String()
#     def mutate(self, info, first_name, last_name, email ="", address="", phone_number=""):
#         user = UserModel(first_name = first_name,
#                          last_name = last_name,
#                          email = email,
#                          address = address,
#                          phone_number = phone_number)
#         return CreateUser(
#             id = user.id,
#             first_name = user.first_name,
#             last_name = user.last_name,
#             email = user.email,
#             address = user.address,
#             phone_number = user.phone_number
#         )
