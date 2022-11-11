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
        use_connection = True



