import graphene
from graphene_django import DjangoObjectType
from ChoLon.models import ProductModel, UserModel
from datetime import timezone

class ProductType(DjangoObjectType):
    class Meta:
        model = ProductModel
        only_fields = (
            'id',
            'pName',
            'pPrice',
            'pQuantity',
            'pDesc',
            'pDateCreated',
        )
        '''
        Create connection for ProductType
        Allow slicing and paginating data in GraphQL
        '''
        use_connection = True

    def resolve_is_old(root, *args):
        return root.pDateCreated < (timezone.now() - timezone.timedelta(days=666))

class UserType(DjangoObjectType):
    class Meta:
        model = UserModel

class CreateUser(graphene.Mutation):
    id = graphene.Int()
    first_name = graphene.String()
    last_name = graphene.String()
    email = graphene.String()
    address = graphene.String()
    phone_number = graphene.String()

    class Arguments:
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()
        address = graphene.String()
        phone_number = graphene.String()
    def mutate(self, info, first_name, last_name, email ="", address="", phone_number=""):
        user = UserModel(first_name = first_name,
                         last_name = last_name,
                         email = email,
                         address = address,
                         phone_number = phone_number)
        return CreateUser(
            id = user.id,
            first_name = user.first_name,
            last_name = user.last_name,
            email = user.email,
            address = user.address,
            phone_number = user.phone_number
        )
class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query = Query,
                         mutation = Mutation
                        )