import graphene
from graphene_django import DjangoObjectType

from graphql_api import models


class User(DjangoObjectType):
    class Meta:
        model = models.User
        fields = (
            "id",
            "name",
            "followers",
        )


class Query(graphene.ObjectType):
    user = graphene.Field(User, id=graphene.Int())

    def resolve_user(self, info, **kwargs):
        id = kwargs.get("id")
        if id is not None:
            return models.User.objects.get(id=id)
        return None


schema = graphene.Schema(query=Query)
