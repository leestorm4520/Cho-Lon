from graphene import Boolean, Field, ID, InputObjectType, Mutation, String, Int
from ChoLon.models import UserModel
# from gql.types import UserType

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserModel
#         fields = (
#             'id',
#             'fName',
#             'lName'
#             'email',
#         )
# class UserInputType(InputObjectType):
#     fName = String()
#     lName = String()
#     email = String()

# class UserCreate(Mutation):
#     class Arguments:
#         input = UserInputType(required = True)
#     user = Field(UserType)

#     def mutate(cls, root, info, **data):
#         serializer = UserSerializer(data = data.get('input'))
#         serializer.is_valid(raise_exception = True)

#         return UserCreate(product = serializer.save())

# class UserDelete(Mutation):
#     class Arguments:
#         id = ID(required = True)

#         ok = Boolean()

#     def mutate(cls, root, info, **data):
#         product = UserModel.objects.get(id = data.get('id'))
#         product.delete()

#         return UserDelete(ok = True)



class UserCreate(Mutation):
    id = Int()
    fName = String()
    lName = String()
    email = String()
    address = String()
    phoneNumber = String()

    class Arguments:
        fName = String()
        lName = String()
        email = String()
        address = String()
        phoneNumber = String()
    def mutate(self, info, fName, lName, email ="", address="", phoneNumber=""):
        user = UserModel(fName = fName,
                         lName = lName,
                         email = email,
                         address = address,
                         phoneNumber = phoneNumber)
        return UserCreate(
            id = user.id,
            fName = user.fName,
            lName = user.lName,
            email = user.email,
            address = user.address,
            phoneNumber = user.phoneNumber
        )
